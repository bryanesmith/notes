# Aerospike notes

## Overview

| Aerospike | RDBM      |
| --------- | --------- |
| namespace | database  |
| set       | table     |
| record    | row       |
| bin       | column    |

* Aerospike is a record-level ("row-oriented") key-value store
    - a **record** is retrieved with a key
    * the record is made up of **bins**

## Architecture

* share-nothing architecture
* Uses a **partition map** to identify which data should be written to which primary node
    - Write to a primary ("master"), which writes to replicas "over the fabric"
* The primary index is an in-memory R-B tree, points to data in RAM or SSD

### XDR

* **XDR**: cross data center prelication. Highly configurable. (e.g., can filter which data goes to which data center)

* Supports multiple topologies:
    - **active/passive**
    - **mesh** (active/active)
    - **star toplogy** (one active that broadcasts out to passive)
    - **linear chain** (`a -> b -> c -> d`)
    - hybrid

### Consistency vs Availability

* namespaces can prioritize availability or consistency
    - **AP mode** (availabile + partition tolerant) is the default mode
    - **strong consistency mode** requires all replicas to be committed
* Specify **replication factor**
* Primary copies data to replica(s), either synchronously as part of put (`write.comment_level = all`) or asynchronously (`write.comment_level = master`)
* **regimes**: during network split, where two nodes think they are the primary, client able to determine the "right" primary (based on large node partition?)
* **flexible reads**: can specify consistency policies at runtime

## CRUD

### Writing data
* Steps to write data: 
    1. digest data to determine **partition ID**
    2. Find the primary node using the partition map
    3. single hop to write the data to the primary node

```java
client.put(
    policy,
    key,
    bin_1,
    bin_2, // ...
)
```

### Reading
* To retrieve a record, need to specify:
    - namespace
    - set
    - key
* Reads are flexible, and support batches as well as selecting which bins to retrun
* Scan operation with `scanCallbacks`
* Secondary index
* Filters (equality, ranges, predicates)
* Supports user defined functions (UDFs)

### Delete
* Data can be removed using 1) TTLs (default is never), 2) deletes
* **Durable deletes** use **tombstones**, and the data is later garbage collected by process call **defragmentation**

## Comparisons

### Aerospike vs Redis

| Similarities | Differences |
| ------------ | ----------- |
| support low latency, high volume | Aerospike 1) more scalable, 2) automatically shards, 3) offers persistence |

| Similarities | Differences |
| ------------ | ----------- |
| Aerospike | Bigtable |
| Low-latency, key-value | Aerospike is row-oriented, Bigtable wide column oriented; Bigtable is potentially more scalable (or at least more elastic?) |