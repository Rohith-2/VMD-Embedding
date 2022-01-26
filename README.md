# VMD-Embedding  
Application of VMD in NLP via TF-IDF for better semantic relationships.

## Publication :
### Conference:
[Proceedings of the 35th Pacific Asia Conference on Language, Information and Computation](http://corpus.shisu.edu.cn/corpusen/PACLIC35/list.htm)
### Paper:
https://aclanthology.org/2021.paclic-1.25/  

## Authors :  
Rohith Ramakrishnan  
[Anirudh Vadakedath](https://github.com/anirudhv14)  
[U Vamsi Krishna](https://github.com/vamsi1609)  
[Premjith B](https://github.com/premjithb)

## Dataset:  

[**IMBD Data**](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) :  
  IMDB dataset having 50K movie reviews for natural language processing or Text analytics.
  This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews    for training and 25,000 for testing.   
  *Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. The 49th Annual Meeting of   the Association for Computational Linguistics (ACL 2011)* 

 > TF-IDF_VMD - Alpha : 6 & K : 2  
 
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.86      | 0.86   | 0.85     | 862     |
  | 1        | 0.86      | 0.85   | 0.86     | 888     |
  | Accuracy |           |        | 0.85     | 1750    |  
  
  > fastText : cc.en.300.bin   
  
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.80      | 0.82   | 0.81     | 875     |
  | 1        | 0.82      | 0.80   | 0.81     | 875     |
  | Accuracy |           |        | 0.81     | 1750    |   

[**Disaster Tweets**](https://www.kaggle.com/c/nlp-getting-started) :  
Natural Language Processing with Disaster Tweets  -  
*This dataset was created by the company figure-eight and originally shared on their ‘Data For Everyone’ website [here](https://www.figure-eight.com/data-for-everyone/)*

 > TF-IDF_VMD - Alpha : 2 & K : 2  
 
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.75      | 0.92   | 0.83     | 1102    |
  | 1        | 0.84      | 0.58   | 0.68     | 802     |
  | Accuracy |           |        | 0.78     | 1904    |  
  
  > fastText : cc.en.300.bin   
 
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.80      | 0.83   | 0.81     | 1098    |
  | 1        | 0.75      | 0.71   | 0.83     | 806     |
  | Accuracy |           |        | 0.78     | 1904    |  
  
  **Covid Tweet**:
   > TF-IDF_VMD - Alpha : 2 & K : 2  
 
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.76      | 0.56   | 0.64     | 944     |
  | 1        | 0.68      | 0.84   | 0.75     | 1056    |
  | Accuracy |           |        | 0.71     | 2000    |  

