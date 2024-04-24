# DeepLearning.AI Short Course: Building and Evaluating Advanced RAG

Started course: 2024/04/23
Taught by: Jerry Liu (**LlamaIndex**) and Anupam Datta (**Truera**)

## Introduction

* **Sentence-window** retrieval and **auto-merging retrieval** may yield better performance than simpler RAG methods

* Useful RAG metrics include **context relevance**, **groundedness**, and **answer relevance**

## Section 1: Advanced RAG Pipeline

* Three components of RAG pipeline:
    1. **Ingestion**: `documents` -> `chunks` -> `embeddings` -> `index`
    2. **Retrieval**: `query` -> `index` -> `top k...`
    3. **Synthesis**: ( `query`, `top k...` ) -> `LLM` -> `Response`

* We're going to set up a basic and advanced RAG pipeline with **LlamaIndex** and an evaluation benchmark with **TruEra**

* **Direct query engine**: how to index and query using `VectorStoreIndex` from `llama_index`: 
    ```py
    from llama_index import Document, ServiceContext, SimpleDirectoryReader, VectorStoreIndex
    from llama_index.llms import OpenAI

    documents = SimpleDirectoryReader(
        input_files=["./eBook-How-to-Build-a-Career-in-AI.pdf"]
    ).load_data()

    document = Document(text="\n\n".join([doc.text for doc in documents]))

    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

    service_context = ServiceContext.from_defaults(
        llm=llm, embed_model="local:BAAI/bge-small-en-v1.5"
    )
    index = VectorStoreIndex.from_documents([document],
                                            service_context=service_context)
    
    query_engine = index.as_query_engine()

    response = query_engine.query(
        "What are steps to take when finding projects to build your experience?"
    )
    ```
    - Note we're using ChaptGPT 3.5 Turbo for LLM and Hugging Face tokenizer
    - `VectorStoreIndex#from_documents` does chunking, embedding, and indexing all at once
    - `VectorStoreIndex.as_query_engine` provides a query engine

* The RAG triad, along with three evaluation metrics:
    ![Diagram of RAG triad](./images/building-and-evaluating-advanced-rag.rag-triad.png)

* Note that our initial simple RAG had decently high groundedness (0.8) and answer relevance (0.93), but poor context relevance (0.26). We'll use more advanced techniques to see if we can get better results.

* **Sentence window retrieval**: replace retrieved sentence with a larger window of surrounding content, to provide more context
    ```py
    from llama_index.llms import OpenAI
    from utils import build_sentence_window_index, get_sentence_window_query_engine

    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

    sentence_index = build_sentence_window_index(
        document,
        llm,
        embed_model="local:BAAI/bge-small-en-v1.5",
        save_dir="sentence_index"
    )

    sentence_window_engine = get_sentence_window_query_engine(sentence_index)

    response = sentence_window_engine.query(
        "how do I get started on a personal project in AI?"
    )
    ```
    - For our example, the sentence window retriever is providing better groundedness (.88 instead of .80), better context relevance (.34 instead of .26), and at lower cost (0.0009 vs 0.003)

* **Auto-merging retrieval**: construct a hierachy (e.g., chunk of size 512) with children nodes (e.g., chunks of size 128). If a parent has majority of children nodes retrieved, we'll replace children nodes with parent node.
    - For our example, the automerging query engine is better across the board

| Architecture | Groundedness | Answer Relevance | Context Relevance | Total Cost |
| ------------ | ------------ | ---------------- | ----------------- | ---------- |
| Direct Query Enging | 0.80 | 0.93 | 0.26 | 0.003 |
| Sentence Window Query Engine | 0.88 | 0.93 | 0.38 | 0.0009 |
| Auto-merging Query Engine | 1.00 | 0.94 | 0.44 | 0.0008 |

## Section 2: RAG Triad of metrics

## Section 3: Sentence-window retrieval

## Section 4: Auto-merging retrieval

## Conclusion