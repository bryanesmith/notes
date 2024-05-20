# Vector Databases: from Embeddings to Applications

## Introduction

* RAG used to overcome inability of LLMs to consider recent or proprietary data without retraining
* Vector databases proceed LLMs, long used for semantic search and recommendation systems

## 1. How to Obtain Vector Representations of Data

* **Autoencorder**: used to encode inputs (e.g., Mnist handwritten digits) into embeddings
    ![Architecture of an autoencoder](images/vector-databases-from-embeddings-to-applications/autoencoder-architecture.png)

* Using `sentence_transformers.SentenceTransformer` to generate embeddings for sentences

* Ways to find the distance between embeddings:

    | Method | Description | Formula | Numpy | Interpretation |
    | ------ | ----------- | ------- | ----- | -------------- |
    | **Euclidean Distance** (L2) | shortest distance between two points or vectors | `√(∑(x-y)^2)` | `np.linalg.norm(a-b), ord=2)` | lower = better match |
    | **Manhattan Distance** (L1) | distance between two points if can only move one axis at a time | `√(∑`&#124;`x - y`&#124;`)` | `np.linalg.norm(a-b), ord=1)` | lower = better match |
    | **Dot Product** | measures the magnitude of the projection of one vector onto the other | `A • B = ∑A*B` | `np.dot(A, B)` | higher = better match (negative values mean far away) |
    | **Cosine Distance** | measures the difference in directionality (the angle) between vectors | `1 - (A • B) / (`&#124;&#124;`A`&#124;&#124;` `&#124;&#124;`B`&#124;&#124;`)` | `1 - (np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))` | lower = better match |

* Dot product and cosine distance are commonly used in NLP (i.e., with sentence embeddings)

## 2. Search for Similar Vectors

* **Semantic search**: looking for embeddings that are similar

* **K Nearest Neighbors** (KNN) is a brute force method for semantic search, and comes with a large computational cost
    - `sklearn.neighbors.NearestNeighbors`
    - KNN doesn't scale; runtimes are hyperlinear (exponential?) for number of embeddings and dimensions

## 3. Approximate Nearest Neighbors

* **Navigable Small World** (NSW) connect each node (say, 2) to nearest nodes to create a graph; and then given a query node, pick a random node in graph, and iteratively navigate to next closest node

* **Hierarchical Navigable Small World** (HNSW) is similar to NSW, but assigns nodes to layers and iteratively works way down layers
    - Lower probability of a node being assigned to higher layers
    - Query time increases logarithmically with number of nodes

* `networkx` library for creating Graphs

* Weaviate (`weaviate`): open source vector database
    - embedded option for running inside notebook

## 4. Vector Databases

* Jeopardy Tiny: `https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json`

* Weaviate can handle vectorization automatically, with multiple choices for **vectorizer** (e.g., `text2vec-cohere`, `text2vec-openai`, etc)
    - E.g., importing Jeopardy Tiny without explicitly vectorizing:
        ```py
        with client.batch.configure(batch_size=5) as batch:
            for i, d in enumerate(data):  # Batch import data
                
                print(f"importing question: {i+1}")
                
                properties = {
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                }
                
                batch.add_data_object(
                    data_object=properties,
                    class_name="Question"
                )
        ```
* Sample semantic search:
    ```py
    response = (
        client.query
        .get("Question",["question","answer","category"])
        .with_near_text({"concepts": "biology"})
        .with_additional(['vector','distance'])
        .with_limit(2)
        .do()
    )
    ```

* Weaviate supports CRUD operations

## 5. Sparse, Dense, and Hybrid Search

## 6. Application - Multilingual Search

## Conclusion 

