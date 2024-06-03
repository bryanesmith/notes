# Section 9: Dockerizing Multiple Services

* We'll create development Dockerfiles for:
    1. React app
    2. Express server
    3. Worker

* Recap: to create development Dockerfiles, we'll basically:
    1. Copy over `package.json`
    2. Run `npm install`
    3. Copy over everything else
    4. Docker compose to set up shared volumes (to support hot reloading)

* Fix environment variable-related issue for Postgres in `docker-compose.yml`:
    ```yaml
      postgres:
        image: "postgres:latest"
        environment:
          - POSTGRES_PASSWORD=postgres_password
    ```
    and run `docker-compose down && docker-compose up --build`

* Two options for specifying environment variables in the `environment` block within a Docker Compose service:
    1. `VARIABLE_NAME=value` if want to store value in `docker-compose.yml`
    2. `VARIABLE_NAME` to pass in variable from your environment (to avoid hard-coding value in `docker-compose.yml`)

* **Path-based routing** with Nginx as a **reverse proxy**:
    - Anything starting with `/api` will be routed to the Express server
    - `default.conf`:
        ```conf
        upstream client {
            server client:3000;
        }

        upstream api {
            server api:5000;
        }

        server {
            listen 80;

            location / {
                proxy_pass http://client;
            }

            location /api {
                rewrite /api/(.*) /$1 break;
                proxy_pass http://api;
            }

            location /ws {
                proxy_pass http://client;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "Upgrade";
            }
        }
        ```
    - **upstream** servers

