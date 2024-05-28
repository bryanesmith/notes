# Section 5: Docker Compose with Multiple Local Containers

- sample docker-compose.yaml file:
    ```yaml
    version: "3"
    services:
        redis-server:
            image: "redis"
        node-app:
            build: .
            ports:
                - "4001:8081"
    ```

- Docker Compose creates a default network; service host names are the service names as declared in `docker-compose.yaml` (e.g., `redis-server`)

- Useful Docker Compose commands:
    ```sh
    % docker-compose up
    % docker-compose up —build
    % docker-compose up -d # background
    % docker-compose down
    % docker-compose ps
    ```


- Automatic container restarts using restart policy (“no”, always, on-failure, unless-stopped). E.g.,
    ```yaml
    …
        node-app:
            restart: always
    ```