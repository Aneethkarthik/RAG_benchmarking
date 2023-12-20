# RAG_Benchmarking
Benchmarking RAG Model

Introduction:

The RAG (Retriever, Answerer, Generator) paradigm has become a crucial framework in information retrieval and natural language processing. A key challenge lies in efficiently retrieving relevant information for language models. Traditionally, cosine similarity has been used in a three-step retriever approach, involving text chunk embedding, query embedding, and ranking based on similarity. However, the effectiveness depends on various factors. This report delves into the complexities of RAG-based information retrieval, exploring challenges and opportunities in the retriever component. It addresses considerations like text embedding methods, chunking strategies, and alternative metrics beyond cosine similarity. Additionally, the report explores hybrid search, combining traditional keyword-based and semantic search for a more comprehensive retrieval approach.

Objective:

The objective of this project is to optimize and enhance the retriever component within the RAG paradigm by conducting comprehensive research, experimentation, and performance evaluation. Specifically, the project aims to achieve the following goals:

1.	Investigate Embedding Techniques: Explore a variety of open-source and paid embedding methods to represent text chunks effectively. Evaluate their performance in information retrieval tasks and identify the most suitable embedder for our retrieval system.
2.	Chunking Strategy Development: Develop a robust text chunking strategy, which may include creating a customized chunking approach, to ensure that text segments are manageable and their sizes remain below 3,000 characters when tokenized with the Tiktoken tokenizer.
3.	Hybrid Search Exploration: Investigate different configurations of hybrid search, which combines traditional keyword-based search with semantic (vector-based) search, to assess the potential advantages it offers in improving retrieval accuracy.
4.	Retriever Function Implementation: Design and implement a retriever function that leverages the selected embedder, chunker, and hybrid search settings. The retriever should effectively retrieve relevant text chunks in response to user queries.
5.	Connect to Evaluation Tool: Integrate the retriever with the provided evaluation tool, allowing the system to calculate precision@k and Mean Reciprocal Rank (MRR) metrics for performance assessment.
6.	Optimization and Evaluation: Continuously iterate and fine-tune the retriever component by experimenting with various combinations of embedders, chunking methods, and hybrid search configurations. Evaluate the retriever's performance using the established evaluation metrics.
7.	Utilize Pinecone for Vector Database: Use the Pinecone platform for managing the vector database, ensuring efficient storage and retrieval of vector representations. Register for a free Pinecone account to facilitate testing and evaluation.




Dataset we used to train the embedding models:

SQUAD V2: Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles.

The types of text embedding models used:

1)	all-mpnet-base-v2 : This is a sentence-transformers model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. We trained this model on SQUADv2 train split and was able to benchmark a mAP@K score of 0.786, where @K is 100 by default.


2)	all-MiniLM-L6-v2: This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search. We trained this model on SQUADv2 train split and was able to benchmark a mAP@K score of 0.772, where @K is 100 by default.

 
3)	E5 Small V2: Text Embeddings by Weakly-Supervised Contrastive Pre-training.. We trained this model on SQUADv2 train split and was able to benchmark a mAP@K score of 0.812, where @K is 100 by default.



4)	bge-base-en-v1.5  : Flag Embedding can map any text to a low-dimensional dense vector which can be used for tasks like retrieval, classification, clustering, or semantic search. And it also can be used in vector databases for LLMs. We trained this model on SQUADv2 train split and was able to benchmark a mAP@K score of 0.792, where @K is 100 by default.
 
 
5)	all-distilroberta-v1: This is a sentence-transformers model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. We trained this model on SQUADv2 train split and was able to benchmark a mAP@K score of 0.789, where @K is 100 by default.

 

 


Considering with respect to MRR score ‘’e5-small-v2’’ model outperforms the other models, moving forward with ‘’e5-small-v2’’ model we have explored different chunking strategies and searching techniques.




Exploring Chunking Strategies with ‘’e5-small-v2’’ model:

1.	Batching: Upsetting vectors into a Pinecone index using a batching strategy with a batch size of 50. This approach optimizes resource utilization, preventing memory constraints by loading only a subset of vectors into memory at a time. The use of smaller batches not only enhances processing speed, reducing latency, but also ensures adaptability to varying dataset sizes. The code's simplicity and adaptability make it well-suited for scenarios where efficient and responsive updates to the index are crucial, providing an effective balance between computational efficiency and memory management.


2.	Hybrid Chunking: It is based on time represents a sophisticated approach to vector index management that integrates temporal considerations into the chunking strategy. This hybrid method dynamically adjusts the boundaries of fixed-size chunks based on temporal factors, accommodating variations in data distribution over time. By considering the temporal dimension, the strategy adapts to the changing characteristics of the dataset, ensuring optimal efficiency in scenarios where the relevance or frequency of data may fluctuate with time. For instance, in applications where the importance of certain information varies across different periods, such as news articles or social media trends, hybrid chunking based on time can enhance the retrieval accuracy by aligning chunk boundaries with temporal patterns. This adaptability enables the system to effectively capture and organize temporal dynamics, resulting in improved responsiveness and relevance in time-sensitive query scenarios.



Hybrid chunking surpasses traditional batching strategies by offering a more adaptive and context-aware approach to vector index management. While batching efficiently processes vectors in predetermined chunks, hybrid chunking introduces dynamic adjustments to chunk boundaries based on evolving data characteristics. This adaptability is especially advantageous in scenarios where dataset dynamics or query patterns change over time. The observed improvement in your score, from 0.32 with batching to 0.34 with hybrid chunking, underscores the efficacy of this strategy.

Searching Techniques:
Default: This approach relies on matching user queries with predefined keywords, a simple yet established method for capturing textual relevance. However, its limitations lie in its inability to grasp the deeper semantic nuances present in natural language. Default search excels in straightforward keyword matching but may struggle with more intricate language structures, potentially missing out on contextually relevant information.

 





Hybrid Search:

Hybrid search is a technique that combines multiple search algorithms to improve the accuracy and relevance of search results. It uses the best features of both keyword-based search algorithms with vector search techniques. By leveraging the strengths of different algorithms, it provides a more effective search experience for users. The Hybrid Search feature was introduced in Weaviate 1.17. It uses sparse and dense vectors to represent the meaning and context of search queries and documents.

 

Why Hybrid Search over Default Searching technique?

Hybrid search, as evidenced by its superior score of 0.47 compared to the default search score of 0.41, emerges as a compelling choice for information retrieval within the RAG paradigm. The traditional default search relies on conventional keyword-based methods, which may struggle to capture the nuanced semantic relationships present in natural language. In contrast, hybrid search strategically combines both keyword and semantic (vector-based) search methodologies. This dual approach leverages the precision of keyword matching while harnessing the depth of semantic understanding offered by vector-based search. The result is a more comprehensive and nuanced retrieval process, where the hybrid model excels in capturing the subtle contextual nuances of user queries.



RESULTS SUMMARY TABLE:

Text embedding models results summary:
Embedding Models	mAP@K Score
all-mpnet-base-v2	0.786
all-MiniLM-L6-v2	0.772
E5 Small V2	0.812
bge-base-en-v1.5  	0.792
all-distilroberta-v1	0.789
	
Based on the above results, model - “E5 Small V2” performs better among all other models that we used. 


Chunking Strategies on e5-small-v2:
Method	Score
Batching	0.32
Hybrid Chunking	0.34
Based on above strategies used “Hybrid Chunking” gives better results


Searching Techniques:
Method	Score
Default	0.41
Hybrid Search	0.47
Based on the above techniques used “Hybrid Search” performs better.


