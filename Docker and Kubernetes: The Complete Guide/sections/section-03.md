# Section 3: Building Customer Images Through Docker Server

* Creating a **Dockerfile** basically involves:
    1. Specify base image
    2. Run commands to install additional programs
    3. Specify command to run on container startup

* **Buildkit** for Docker Desktop
    - Enabled by default in more recent versions of Docker
    - To enable more progress info:
        ```bash
        % docker build --progress=plain .
        ```
    - To disable cache:
        ```bash
        docker build --no-cache --progress=plain .
        ```
    - To disable Buildkit:
        ```bash
        % DOCKER_BUILDKIT=0 docker build .
        ```

* Creating a Docker image for running redis-server:
    1. Create project folder: 
        ```bash
        % mkdir redis-image
        % cd redis-image
        ```
    2. Create and populate `Dockerfile`. E.g., [this Dockerfile](../projects/redis-image/Dockerfile):
        ```dockerfile
        # base image
        FROM alpine

        # dependencies
        RUN apk add --update redis

        # command
        CMD ["redis-server"]
        ```
    3. Run:
        ```bash
        % docker build . # look for 'writing image sha256:<image-id>'
        ```

* Docker **instructions**:
    - `FROM`: use a base image
    - `RUN`: run a command (e.g., install dependencies)
    - `CMD`: specify command to run on container startup
    - Will cover more later

* **Build context**: the set of files and folders to wrap in a container, specified in the `docker build .` command

* `apk` is the default package manager for Alpine Linux

* **Intermediate containers**: each instruction (besides `FROM`) generates a temporary container for completing the instruction, and after snapshotting the filesystem the container is removed

* Rebuilds with a cache: While building an image that contains unmodified identical steps, Docker will reuse images from a cache for every step until a new instruction is encountered

* **Tags**:
    ```bash
    % docker build -t bryanesmith/myproject:latest .
    % docker run bryanesmith/myproject # or 'bryanesmith/myproject:latest'
    ```
    - Technically, only the version at the end is the 'tag', though the entire process is called "tagging"

* Though you probably won't use this much (or ever), here's how you can create an image from a container using `docker commit`:
    1. Start a running container:
        ```sh
        % docker run -it alpine sh
        ```
    2. Manually install Redi:
        ```sh
        # apk add --update redis
        ```
    3. In another terminal, run:
        ```sh
        % docker ps
        ...
        % docker commit -c 'CMD ["redis-server"]' <container-id>
        sha256:<image-id>
        ```