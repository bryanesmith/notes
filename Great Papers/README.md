# Great Papers

## 2024

### [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits](https://arxiv.org/abs/2402.17764) by Ma et al (8pp)

### [Hallucination is Inevitable: An Innate Limitation of Large Language Models](https://arxiv.org/abs/2401.11817) by Xu et al (26pp)

## 2021 

### [Power of data in quantum machine learning](https://www.nature.com/articles/s41467-021-22539-9) by Huang et al (9pp)

### [TensorFlow Quantum: A Software Framework for Quantum Machine Learning](https://arxiv.org/pdf/2003.02989.pdf) by Broughton et al (56pp)

## 2020

### [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361.pdf) by Kaplan et al (30pp)

## 2019 

### [Quantum supremacy using a programmable superconducting processor](https://www.nature.com/articles/s41586-019-1666-5) by Arute et al (7pp)

## 2018

### [Deep Contextualized Word Representations](https://aclanthology.org/N18-1202.pdf) by Peters et al (11pp)

* Shows that deep contextualized word embeddings can out perform static word embeddings in NLP tasks

## 2017

### [Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) by Vaswani et al (11pp)

Key concepts:

* Transformers are able to outperform other sequence transduction models while requiring fraction of computation
* Transformers generalize well to other tasks, even without task-specific tuning; in this case, a model trained for translation performed very well for constituency parsing
* Transformers achieve these with a unique architecture: unlike other dominant sequence transduction models, which combine attention with recurrence or convolution, the transformer exclusively uses attention. This removes the sequential bottleneck of recurrence (where hidden states depend on prior hidden states) and high computational complexity of convolutions
* Additionally, unlike other models, transformers are able to relate distant tokens as easily as neighboring tokens

Useful vocabulary:

| Vocab | Meaning |
| --- | --- |
| **backpropagation through time** (**BPTT**) | |
| **RELU** | neural network activation function `g(x) = max(0, x)`, which is computationally easy and less susceptible to vanishing gradient problem |
| **bidirectional neural networks** | neural networks where nodes subsequently use their own outputs as inputs |
| **self-attention** | using the dot-product of word embeddings with all other embeddings for words in sentence to generate a new embedding with more context |
| **SoftMax** | scales numbers into probabilities that add up to 1. `a_i = exp(S_i) / ∑_j exp(S_j)` |
| **attention** | see below | 
| **multi-head attention** | including multiple attention mechanisms to enable each to specialize on specific functions and semantics, and hence provide better overall performance |
| **transduce** | convert from one form to another. (E.g., `Audio signial` -> `Transducer` -> `Electricity signal`) |
| **transductive inference** | predicting specific exaples of an unknown function (as opposed to **inductive learning**, which derives the actual function) |
| **positional encodings** | encodings of same size of semantic encodings that provide essential positional context |
| **label smoothing** | regularization technique that adds noise to labels, to account for fact that datasets contain mistakes |
| **NVIDIA P100 GPUs** | high-end GPUs intended for datacenters designed specifically for deep learning training, optimized for more intence computations |
| **Adam optimizer** | Easy-to-tune, space- & compute- efficient, scalable extension to stochastic gradient descent |
| **BiLingual Evaluation Understudy** (**BLEU**) | score between 0 and 1 that measures similarity of machine learning text to set of high quality reference translations |
| **constituency parsing** | NLP task where sentence is segregated into constituents, or groups of words, based on grammatical roles (e.g., noun phrases, verb phrases) |

* **attention**:  `attention(q,k,v) = ∑_i similarity(q, k_i) * v_i`
    - query (q):  the embedding of word we want context for
    - key (k): the set of all word embeddings that could be related (e.g., in same sentence)
    - value (v): the output embeddings
    - think of attention as an information retrieval process, like a database; except it returns weighted combination of values instead of a single value

### [Meet Michelangelo: Uber’s Machine Learning Platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/) by Hermann

### [Spanner, TrueTime and the CAP Theorem](https://research.google/pubs/pub45855/) by Brewer (7pp)

### [Understanding Deep Learning Requires Rethinking Generalization](https://arxiv.org/pdf/1611.03530.pdf) by Zhang et al (15pp)

## 2016

### [Design patterns for container-based distributed systems](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45406.pdf) by Burns and Oppenheimer (6pp)

### [Security Keys: Practical Cryptographic Second Factors for the Modern Web](https://research.google/pubs/pub45409/) by Lang et al (16pp)

### [TensorFlow: A system for large-scale machine learning](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf) by Abadi et al (20pp)

## 2015

### [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](http://proceedings.mlr.press/v37/ioffe15.pdf) by Ioffe and Szegedy (9pp)

### [Deep Learning](https://www.researchgate.net/publication/277411157_Deep_Learning) by LeCun et al (9pp)

### [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) by He et al (12pp)

### [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) by Sculley et al (9pp)

### [Kafka, Samza and the Unix Philosophy of Distributed Data](https://martin.kleppmann.com/papers/kafka-debull15.pdf) by Kleppmann and Kreps (11pp)

### [Turning the database inside-out with Apache Samza](https://www.confluent.io/blog/turning-the-database-inside-out-with-apache-samza/) by Kleppman

## 2014

### [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) by Kingma, Ba (15pp)

### [Don’t count, predict! A systematic comparison of context-counting vs. context-predicting semantic vectors](https://aclanthology.org/P14-1023.pdf) by Baroni et al (10pp)

* Influential paper that showed that prediction-based word models outperformed count-based word models by a large margin on various language tasks.

### [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf) by Srivastava et al (30pp)

### [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf) by Pennington et al (12pp)

* Standord embedding technique emerged as alternative to Google's word2vec

### [Questioning the Lambda Architecture](https://www.oreilly.com/radar/questioning-the-lambda-architecture/) by Kreps

## 2013

### [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) by Mikolov et al (12pp)

* Influential word2vec paper

Key concepts:

* Two new techniques that demonstrate ability to generate highly accurate (state-of-the-art) word vectors using simple model architecture, which due to lower computational complexity enables use of much larger data set
* Simple techniques are often good enough with lots of data, but when "lots of data" isn't possible, need enhanced techniques
* Goal of this paper is to scale to millions of vocab with billions words in dataset
* Word embeddings enable vector algebra; e.g., "king" - "man" + "woman" ~= "queen"
* Common for model developers to increase size without increasing vector dimension, but need to increase both to avoid diminishing returns
* Two novel architectures: (1) **Continuous Bag of Words** (**CBOW**), which predicts target word given context words in sentence; (2) **Skip-gram**, which preicts context words given input word. Both use a single hidden layer neural network followed by a softmax layer, and the model outputs don't matter - its the weights on the hidden layer that are the word embeddings!
* Skip-gram has all-around better performance, but CBOW is faster to train & may be better at some tasks

Useful vocabulary:

| Vocab | Meaning |
| --- | --- |
| **word representation** | translation of raw text into vector format |
| **label encoding** | assigning sequential values to categorical data so models can interpret. Easy, but can result in unintended bias for data with higher numbers. (One-hot encoding addresses issue but results in sparse vectors & explosion of number of features) |
| **static embedding** vs **contextualized word representations** | word2vec is an example of fomer; latter handle out-of-vocabulary words, rare words, and polysemy better |
| **polysemy** | ability of word to take on different meanings in different contexts |
| **argmax** | find argument that gives maximum vlaue of target function |
| **count-based work models** vs **prediction-based word models** | |
| **hierarchical softmax** (**H-Softmax**) | Replaces flat softmax layer with a binary-tree like approximation that speeds up word prediction tasks 50x or more |
| **Huffman binary tree** | Enables lossless data compression by building a tree with shortest length paths for more frequently use words, and assigning variable length codes to input characters |


### [Distributed Representations of Words and Phrases and their Compositionality](https://proceedings.neurips.cc/paper_files/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf) by Mikolov et al (9pp)

* Influential word2vec paper

## 2012

### [CAP Twelve Years Later: How the "Rules" Have Changed](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) by Eric Brewer

### [Searching for Build Debt: Experiences Managing Technical Debt at Google](https://research.google/pubs/pub37755/) by Morgenthaler et al (6pp)

## 2011

### [Kafka : a Distributed Messaging System for Log Processing](https://www.semanticscholar.org/paper/Kafka-%3A-a-Distributed-Messaging-System-for-Log-Kreps/ea97f112c165e4da1062c30812a41afca4dab628) by Kreps (7pp)

### [Scikit-Learn: Machine Learning in Python](https://www.jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf) by Pedregosa et al (6pp)

## 2010

### [Availability in Globally Distributed Storage Systems](https://research.google/pubs/pub36737/) by Ford et al (14pp)

## 2007 

### [Dynamo: Amazon's highly available key-value store](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store) by DeCandia et al (16pp)

* Will Larson said this may be _the_ classic modern systems paper, with good introduction on eventual consistency

### [On Designing and Deploying Internet-Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf) by James Hamilton (12)

## 2006

### [Bigtable: A Distributed Storage System for Structured Data](https://research.google/pubs/pub27898/) by Chang et al (14pp)

### [Out of the Tar Pit](https://www.semanticscholar.org/paper/Out-of-the-Tar-Pit-Moseley-Marks/41dc590506528e9f9d7650c235b718014836a39d) by Moseley and Marks (66pp)

## 2004

### [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/pub62/) by Jeffrey Dean Sanjay Ghemawat (13pp)

## 2003

### [The Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) by Ghemawat et al (15pp)

## 2001

### [Greedy Function Approximation: A Gradient Boosting Machine](https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boosting-machine/10.1214/aos/1013203451.full) by Friedman (44pp)

* origin of term "gradient boosting"

### [Random Forests](https://link.springer.com/content/pdf/10.1023/A:1010933404324.pdf) by Breiman (28pp)


## 1999

### [Big Ball of Mud](http://www.laputan.org/mud/) by Foote and Yoder

### [Harvest, Yield, and Scalable Tolerant Systems](https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf) by Fox and Brewer (5pp)

* Will Larson says this builds on "CAP Twelve Years Later", and introduces concepts of "harvest" and "yield"

## 1996

### [Bagging Predictors](https://link.springer.com/content/pdf/10.1007/BF00058655.pdf) by Breiman (18pp)

### [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/pdf/quant-ph/9508027.pdf) by Peter W. Shor (28pp)

## 1995

### [Support-Vector Networks](https://link.springer.com/content/pdf/10.1007/bf00994018.pdf) by Cortes and Vapnik (25pp)
 
## 1986

### [Learning representations by back-propagating errors](https://gwern.net/doc/ai/nn/1986-rumelhart-2.pdf) by Rumelhart et al (4pp)

## 1985

### [The case for shared nothing](https://www.semanticscholar.org/paper/The-Case-for-Shared-Nothing-Stonebraker/a05d78d262792b22a66b7b15b2330e380318c830) by Stonebraker (5pp)

## 1983

### [Hints for Computer System Design](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/acrobat-17.pdf) by Lampson (27pp)

* Will Larson said this is a phenomenal overview of systems design
 
### [Principles of transaction-oriented database recovery](https://dl.acm.org/doi/10.1145/289.291) by Reuter and Härder (31pp)

* coined the acronym "ACID" 

# 1974

### [The UNIX time-sharing system](https://dl.acm.org/doi/10.1145/361011.361061) by Ritchie and Thompson (11pp)

## 1949

### [The Organization of Behavior](https://pure.mpg.de/rest/items/item_2346268_3/component/file_2346267/content), Donald O. Webb (365pp)


















