import os
import numpy as np
import pandas as pd
import scipy.signal
from tqdm import tqdm
from vmdpy import VMD
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

class TFVMD():
      
      def _init__(self,alpha = 2, tau = 0, K=2, DC = 0, init=1, tol=1e-8):
            self.alpha = alpha 
            self.tau = tau
            self.K = K
            self.DC = DC
            self.init = init
            self.tol = tol
            
      # From the given modes, using the SciPy
      # package the mode containing the maximum
      # energy will be selected.
      def energy(self.u):
            
          # Estimate PSD `S_xx_welch` at discrete frequencies `f_welch`
          f_welch, S_xx_welch = scipy.signal.welch(u)
          
          # Integrate PSD over spectral bandwidth
          # to obtain signal power `P_welch`
          df_welch = f_welch[1] - f_welch[0]
          return np.sum(S_xx_welch) * df_welch


      def maxvdm(self,f):
            
          u, u_hat, omega = VMD(f, self.alpha, self.tau, self.K, self.DC, self.init, self.tol) 
          energy_array=[]
          for i in u:
              energy_array.append(self.energy(i))
          ind = np.argmax(energy_array)
          return u[ind]
      

       def fit(self,X):
            X = train.tolist()
            
            # Computing the TF-IDF vectors from the given corpus of training data
            print("Computing TF-IDF..")
            tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
            self.features = tfidf.fit_transform(X).toarray()
            
            print("Extracting Modes..")
            X_data = [self.maxvdm(i) for i in tqdm(self.features)]
            
            return self.X_data

        def fit_csv(self,path,sep=','):
            train = pd.read_csv(path,sep)
            return self.fit(train)
      
      
