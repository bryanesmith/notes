# Section 6: Creating a Production-Grade Workflow

- Our workflow: 
    1. Develop using a development container (using Docker volumes to enable live reload)
    2. Commit changes to feature branch
    3. TravisCI 
    4. `main` branch
    5. AWS Elastic Beanstalk 

- Install Node v8.11.3

- Generate our React app:
    ```sh
    % npx create-react-app frontend
    ```

- useful commands:
    ```sh
    % npm run start
    % npm run test
    % npm run build
    ```

- To run Docker files with custom Dockerfile name:
    ```sh
    % docker build -t bryanesmith/frontend -f Dockerfile.dev . 
    % docker run -p 3000:3000 bryanesmith/frontend
    ```

- **Docker Volumes**:
    - Command:
        ```sh
        % docker run -p 3000:3000 -v /app/node_modules -v "$(pwd):/app" bryanesmith/frontend
        ```
    - Note:
        - `-v a/app/node_modules` puts a **bookmark** on `/app/node_modules` folder in container, meaning it won't be mapped
        - `-v $(pwd)/app` maps the present working directory to `/app` in container

- Using Docker Compose with volumes:
    ```yaml
    version: '3'
    services:
    web:
      build:
        context: .
        dockerfile: Dockerfile.dev
      ports: 
        - "3000:3000"
      volumes: 
        - /app/node_modules
        - .:/app
    ```

- Refresher:
    ```bash
    % docker-compose up
    ```

- To run tests using `docker run`:
    ```bash
    % docker build -t bryanesmith/frontend -f Dockerfile.dev . 
    % docker run bryanesmith/frontend npm run test      # no stdin nor psuedo terminal
    % docker run -it bryanesmith/frontend npm run test  # no live updates
    % docker run -it -v /app/node_modules -v "$(pwd):/app" bryanesmith/frontend npm run test
    ```

* Options for running tests:
    1. Using `docker run`:
        ```bash
        % docker run -it -v /app/node_modules -v "$(pwd):/app" bryanesmith/frontend npm run test
        ```
        - Cons: a lot to type out
    2. Attaching to a container to manually run tests:
        ```bash
        % docker-compose up
        % # or: docker run -it -v /app/node_modules -v "$(pwd):/app" bryanesmith/frontend
        % 
        % # then, in another terminal:
        % docker ps     # get id for running container
        % docker exec -it e5271faedee9 npm run test
        ```
        - Cons: more complex (find container image, second termal, three commands)
    3. Adding a service via Docker Compose 
        ```yaml
        version: '3'
        services:
        web:
            build:
            context: .
            dockerfile: Dockerfile.dev
            ports: 
            - "3000:3000"
            volumes: 
            - /app/node_modules
            - .:/app
        tests:
            build:
            context: .
            dockerfile: Dockerfile.dev
            volumes: 
            - /app/node_modules
            - .:/app
            command: ["npm", "run", "test"]
        ```
        ```bash
        % docker-compose up --build
        ```
        - Cons: no stdin, test and application output interleaved 

* **Multi-stage builds** are useful when:
    - Want to use different images for build vs deploy (e.g., `node:alpine` to use `npm build`, but `xxx` to run nginx)
    - Don't want to copy over development dependencies (bloat and security risks)

* 
    ```DOCKERFILE
    # >>> STAGE 1: build <<<
    FROM node:16-alpine as builder
    WORKDIR '/app'

    # install dependencies
    COPY package.json .
    RUN npm install

    # build website -> /app/build
    COPY . .
    RUN npm run build

    # >>> STAGE 2: deploy <<<
    FROM nginx
    COPY --from=builder /app/build /usr/share/nginx/html
    # default command of nginx container will start the server, so no CMD required
    ```
    ```bash
    % docker build .
    % docker run -p 8080:80 048eb08a35 
    ```