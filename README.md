# VMD-Embedding  
Application of VMD in NLP via TF-IDF for better semantic relationships.  

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

 > TF-IDF_VMD - Alpha : 2 & K : 3  
 
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.86      | 0.77   | 0.81     | 875     |
  | 1        | 0.79      | 0.88   | 0.83     | 875     |
  | Accuracy |           |        | 0.82     | 1750    |  
  
  > fastText : cc.en.300.bin   
  
  |          | precision | recall | f1-score | support |
  |----------|-----------|--------|----------|---------|
  | 0        | 0.80      | 0.82   | 0.81     | 875     |
  | 1        | 0.82      | 0.80   | 0.81     | 875     |
  | Accuracy |           |        | 0.81     | 1750    |   

[**train.csv**](https://www.kaggle.com/c/nlp-getting-started) :  
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

## References:  
```
Vinícius R. Carvalho, Márcio F.D. Moraes, Antônio P. Braga, Eduardo M.A.M. Mendes, Evaluating five different adaptive decomposition methods for EEG signal seizure detection and classification, Biomedical Signal Processing and Control, Volume 62, 2020, 102073, ISSN 1746-8094, https://doi.org/10.1016/j.bspc.2020.102073.   

 Brill E. (2003) Processing Natural Language without Natural Language Processing. In: Gelbukh A. (eds) Computational Linguistics and Intelligent Text Processing. CICLing 2003. Lecture Notes in Computer Science, vol 2588. Springer, Berlin, Heidelberg. https://doi.org/10.1007/3-540-36456-0-37. 

Rajaraman, A.; Ullman, J.D. (2011). "Data Mining" (PDF). Mining of Massive Datasets. pp. 1–17. doi:10.1017/CBO9781139058452.002. ISBN 978-1-139-05845-2.  

Luhn, Hans Peter (1957). "A Statistical Approach to Mechanized Encoding and Searching of Literary Information" (PDF). IBM Journal of Research and Development. 1 (4): 309–317. doi:10.1147/rd.14.0309.  


Dragomiretskiy Konstantin, Dominique Zosso Variational mode decomposition. IEEE Transactions on Signal Processing, Vol. 62, 2014, p. 531-544.  

A. O. Boudraa, and J. C. Cexus, “Denoising via empirical mode decomposition", in Proc. ISCCSP 2006.  

B. Weng, M. Blanco-Velasco, and K. E. Barner, "ECG Denoising Based on the Empirical Mode Decomposition", Proceedings of the 28th IEEE EMBS Annual International Conference New York City, USA, Aug 30-Sept 3, 2006. A. Boudraa, and J. C. Cexus, "EMD-Based signal filtering", IEEE Trans. on Instrumentation and measurement, vol. 56, no. 6, Dec2007.  

K. Khaldi, M. Turki-Hadj Alouane, A.-O. Boudraa, "A new EMD denoising approach dedicated to voiced speech signals", Signals, Circuits and Systems, 2008. SCS 2008. 2nd International Conference on Volume, Issue 7-9 Page (s): 1-5, Nov. 2008.  

Hamid et al, "Empirical Mode Decomposition for advanced speech signal processing”, Journal of Sig. Processing, vol. 17, no. 6, pp. 215-229, Nov 2013.  

Zhu, "Anovel multiscale ensemble carbon price prediction model integrating empirical mode decomposition, genetic algorithm and artificial neural networks”. Energy Economies, 2012.  

Suryani Lim, Henri Prade, Gilles Richard, Classifying and completing word analogies by machine learning, International Journal of Approximate Reasoning, Volume 132,2021,Pages 1-25,ISSN 0888-613X, https://doi.org/10.1016/j.ijar.2021.02.002. (https://www.sciencedirect.com/science/article/pii/S0888613X21000141). 

A. Ferrari, B. Donati and S. Gnesi, "Detecting Domain-Specific Ambiguities: An NLP Approach Based on Wikipedia Crawling and Word Embeddings," 2017 IEEE 25th International Requirements Engineering Conference Workshops (REW), Lisbon, 2017, pp. 393-399, doi: 10.1109/REW.2017.20.  

Seyed Mahdi Rezaeinia, Ali Ghodsi and Rouhollah Rahmani, "Improving the Accuracy of Pre-trained Word Embeddings for Sentiment Analysis". arXiv, 2017.   

Balakrishnan, Barathi Ganesh Hullathy and Vinayakumar, Anand Kumar Madasamy and Padannayil, Soman Kotti, "NLP CEN AMRITA@ SMM4H: Health Care Text Classification through Class Embeddings".  

K. Soman and Anand Kumar M, "Amrita-CEN@ MSIR-FIRE2016: Code-mixed question classification using BoWs and RNN embeddings". FIRE (Working notes), 122--125, 2016.  

J. Martineau et al., “Delta TFIDF: An Improved Feature Space for Sentiment Analysis,” Proc. Second Int. Conf. Weblogs Soc. Media (ICWSM, vol. 29, no. May, pp. 490–497, 2008.  

G.Rilling,P.Flandrin,and P.Gonçalvès,“On empirical mode decomposition and its algorithms,” in Proc. IEEE-EURASIP Workshop Non- linear Signal Image Process. (NSIP), 2003, vol. 3, pp. 8–11.  

Jones, Karen Sparck. "A statistical interpretation of term specificity and its application in retrieval." Journal of documentation, 1972.
