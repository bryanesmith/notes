# Section 10: A Continuous Integration Workflow for Multiple Images

* Our multi-container workflow:
    1. Push code to GitHub
    2. TravisCI automatically pulls repo
    3. Travis builds a test image, tests code
    4. Travis builds prod images
    5. Travis pushes built prod images to Docker Hub
    6. Travis pushes project to AWS Elastic Beanstalk
    7. Elastic Beanstalk pulls images from Docker Hub, serves

* Travis will:
    1. Specify docker as a dependency
    2. Build test version of React project
    3. Run tests
    4. Build prod versions of all projects
    5. Push all to Docker Hub
    6. Tell Elastic Beanstalk to update