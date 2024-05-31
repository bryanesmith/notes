# Section 8: Building a Multi-Container Application

* Limitations of our previous Docker projects:
    1. App was simple, with no outside dependencies
    2. Our image was built multiple times
    3. How do we connect to a database from a container?

* Our over-the-top Fibonacci calculator web application architecture:
    - Nginx
    - React Server (frontend requests)
    - Express Server (backend API requests)
    - Redis (will store "Calculated Values")
    - Worker node (watches Redis for new indices, calculates new value then puts it back in Redis)
    - Postgres (will store "Values I have seen")

* `complex` project subdirectories:
    - `worker`: Node-based worker listening for new Fibonacci requests and fulfilling them asynchronously
    - `server`: Express-based API server
    - `client`: React application