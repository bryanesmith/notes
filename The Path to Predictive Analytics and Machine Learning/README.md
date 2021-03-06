# The Path to Predictive Analytics and Machine Learning
Conor Doherty, Steven Camina, Gary Orenstein, Kevin White

## Notes

* Available as a [free download](http://www.oreilly.com/data/free/the-path-to-predictive-analytics-and-machine-learning.csp)
* Written exclusively by employees of MemSQL, a distributed, in-memory database

## 1: Building Real-Time Data Pipelines

* **Operational applications** (automatic decision making) vs **interactive applications** (computer-aided decision making) (1)
* Domain-specific languages like R generally not suitable for low-latency production envs (1)
* Starts w/ high-through messaging system (e.g., Kafka), then the transformation tier (incl enrichment, filtering, aggregation; e.g., Spark streaming), the persistent datastore (2-4)
* Traditionally, OLTP (real-time data) and OLAP (historical data) are siloed, and moving data between them requires ETL. This siloing prevents real-time application. (5-6)

## 2: Processing Transactions and Analytics in a Single Database

* Memory optimized datastore allow concurrent, transactional read-write access; in-memory is necessary, as disk-backed cannot deliver necessary I/O (8)
* Our hybrid data system must allow us to compare real-time data (high-throughput operational transactions) to aggregations of historical data (fast analytical queries) (8)
* **Compiled query execution plans**: executing query directly in memory avoids code generation and hence improves query performance (8-9)
* **Multiversion Concurrency Control** (MVCC) avoids locks on reads and writes (9)
* Durability and high availability essential (11-12)

## 3: Dawn of the Real-Time Dashboard

* E.g., Tableau (18), Zoomdata (19), Looker (19-20)

## 4: Redeploying Batch Models in Real Time

* **Lambda architecture** handles high volumes of data by combining batch processing and stream processing (24-25)
  - *batch layer* (e.g., Hadoop) stores events and produces *batch views*
  - *speed layer* (e.g., Storm, Spark) deals with recent data only
  - *serving layer* responds to queries and merges results from batch and speed layers

## 5: Applied Introduction to Machine Learning

* Choosing proper ML technique requires evaluating series of tradeoffs, e.g., training and scoring latency, bias and variance, sometimes accuracy versus complexity (29)
* **Supervised learning** involves training data that includes **features** (observations) and **labels** (outcomes) (30)
* **Regression models** are supervised learning that output values in a continuous space, where as **classification models** are in a discrete space (31)
* **Overfitting** approaches zero error and fails to account for variance in natural data; **underfitting** occurs when too much bias in model (31)
* Linear, polynomial, logistic regression (31-32)
* Choice of error function has big impact on result (33)
* **Least squares** is most common error function; involves minimization of sum of squares (33)
* Variants such as weighted least squares, which gives more emphasis to some data (34)
* **Regularization** is a family of techniques that avoid overfitting by associating a cost with complexity (34)
* Two sources of error: **bias** (flawed assumptions in model) and **variance** (noise in the dataset) (34)
  - bias-variance tradeoff
* **Unsupervised learning** involves unlabeled training data; the goal is to discern patterns in data that are not known beforehand (35-36)
* **Semi-supervised learner**: e.g., using unsupervised algorithm to classify customers in order to build a supervised classification model (36)
* **Cluster Analysis** detect patterns in grouping of data; e.g., centroid-based techniques like k-means analysis (37)

## 6: Real-Time Machine Learning Applications

* Most data analysis tools are interactive, and they are useful for development, but their latency is too high for production use; requires real-time (low-latency) scoring (38-40)
* If real-world factors change frequently enough, production system may be bound by **training latency** rather than **scoring latency** (40)
* Fast training requires in-memory storage, access to real-time and historic data, convergence of systems (40-41)
* Real-time anomaly detection one of most promising real-time unsupervised learning applications; e.g., internet security (42)
* Real-time clustering; e.g., discovering related content (43)

## 7: Preparing Data Pipelines for Predictive Analytics and Machine Learning

* Separate stream processing, transactions, and analytics were motivated by disk-based, single-machine systems (46)
* Key to designing real-time predictive analytics systems in to minimize data movement (47)
* Often, a scoring model can be implemented in pure SQL; moving computations to database reduces data movement (48)
* **Dimensionality reduction**, **feature selection** (48)
* **Principal Component Analysis** (PCA) is a dimensionality reduction technique that maps data to lower dimensional space while preserving as much variance as possible while removing features contributing little variance (48)

## 8: Predictive Analytics in Use

* Industrial Internet of Things (IIoT) for improving operational efficiency (51)
* PowerStream simulates the tracking of ~20k wind turbines world wide, receiving between 1-2M inserts/second, costing $19k on AWS; the goal is to predict wind turbine health (52)
* **SQL pushdown**: pushing down execution of query into database (e.g., using MemSQL RDD) can achieve of speeds of a few seconds for operations that may otherwise take half an hour (59)

## 9: Techniques for Predictive Analytics in Production

* Querying schemaless data (e.g., json) above tens of thousands will add query latency; can use computed columns to extract values at time of insert (and optionally index): (73)
  ```SQL
  CREATE TABLE events (
    event JSON NOT NULL,
    user_id AS event::$user_id PERSISTED INT,
    price AS event::$purchase_price PERSISTED FLOAT );
  ```
* Can segment data by event type for query performance reasons, especially when certain types of events (e.g., purchase) far less frequent than others (e.g., views); can create views to join the tables (74)
* Using **upserts** (`INSERT ... ON DUPLICATE KEY UPDATE ...`) to store real-time aggregate statistics (75)
* **Feature scaling** frequently involves subtracting feature-wise mean and dividing by feature-wise standard deviation; can improve performance, and prevents features from disproportionately influencing model (75)
  - This can be hardcoded in the database as a view (76)
* "Online" in ML sense refers to class of algorithms that can be updated iteratively as data becomes available (76)

## 10: From Machine Learning to Artificial Intelligence

* Data science emerged from statistics as data became cheaper, and computing power grew and declined in cost (79-80)
* Machine learning steps ahead of statistics in its ability to generate iterative tests; e.g., random forests, which prevents overfitting (80)
* Machine learning also deals better with complex trends and non-normal distributions (81-82)
* Challenge for ML and AI: resource management for algorithms that are not closed-loop (83)
