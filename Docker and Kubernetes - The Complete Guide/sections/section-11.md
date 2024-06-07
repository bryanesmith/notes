# Section 11: Multi-Container Deployments to AWS

* Creating a `Dockerrun.aws.json` file to configure Elastic Beanstalk (EBS) 
    - Made up of **container definitions**
    - Configure it to (a) work with multiple Docker images, (b) pull the image from Docker Hub instead of building the image
    - Elastic Beanstalk uses Elastic Container Service (ECS) behind the scense to run containers, and ECS **task definitions** are basically the same as container definitions in EBS

* Replacing our Redis and Postgres Docker containers with **AWS Elastic Cache** and **AWS Relational Database Service** (**RDS**), because:
    - Elastic Cache automatically creates, scales, and maintains Redis, and provides better security and migration paths off Elastic Beanstalk
    - RDS automatically creates databases, provides easy scalability, automatically backs up and provides rollbacks, and provides better security and migration paths off Elastic Beanstalk 