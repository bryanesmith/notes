# Section 7: Continuous Integration and Deployment with AWS

* Travis CI will:
    1. Create a development container using `Dockerfile.dev` (feature branch)
    2. Run tests
    3. Build production container using `Dockerfile` (main branch)
    4. Deploy our production container to AWS Elastic Beanstalk 

* To run tests non-interactively:
    ```sh
    % docker run -e CI=true bryanesmith/docker-react npm run test
    ```

* Sample `.travis.yml` file:
    ```yaml
    sudo: required
    services:
    - docker

    before_install:
    - docker build -t bryanesmith/docker-react -f Dockerfile.dev .

    script:
    - docker run -e CI=true bryanesmith/docker-react npm run test
    ```

* To configure Elastic Beanstalk:
    1. Creating EC2 Instance Profile
    2. Elastic Beanstalk Environment Creation
    3. S3 Bucket Configuration
    4. Required Updates for Docker Compose

* To pass a specific filename for running Docker Compose:
    ```bash
    % docker-compose -f docker-compose-dev.yml up
    ```