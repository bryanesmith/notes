# Section 4: Making Real Projects with Docker

* High-level steps for creating our Node.js-based web application:
    1. Create Node.JS web app
    2. Create Dockerfile
    3. Build image from Dockerfile
    4. Run image as container

* Reminders about Buildkit:
    1. To see progress info: `docker build --progress=plain .`
    2. To not use cache: `docker build --no-cache --progress=plain .`
    3. To disable Buildkit: `DOCKER_BUILDKIT=0 docker build .`

* Node.js refresher:
    1. To install deps: `npm install`
    2. To start server: `npm start`

* Recap: to build a tagged image and run it as a container:
    ```sh
    % docker build -t bryanesmith/simpleweb .
    % docker run bryanesmith/simpleweb
    ```

* To set up **port forwarding**:
    ```sh
    % # docker run -p <local_host_port>:<container_port> <image_id>
    % docker run -p 8080:8080 bryanesmith/simpleweb
    ```

* Recap: to debug your containers:
    ```sh
    % docker run -it bryanesmith/simpleweb sh
    ```