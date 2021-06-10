#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import scipy.signal

from vmdpy import VMD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score


train = pd.read_csv('train.tsv',sep='\t')



def format_text(df,col):
  #Remove @ tags
  comp_df = df.copy()
    
  # remove all the punctuation
  comp_df[col] = comp_df[col].str.replace(r'(@\w*)','')

  #Remove URL
  comp_df[col] = comp_df[col].str.replace(r"http\S+", "")

  #Remove # tag and the following words
  comp_df[col] = comp_df[col].str.replace(r'#\w+',"")

  #Remove all non-character
  comp_df[col] = comp_df[col].str.replace(r"[^a-zA-Z ]","")

  # Remove extra space
  comp_df[col] = comp_df[col].str.replace(r'( +)'," ")
  comp_df[col] = comp_df[col].str.strip()

  # Change to lowercase
  comp_df[col] = comp_df[col].str.lower()
  comp_df[col] = comp_df[col].str.replace('httpurl', '')
  return comp_df



train = format_text(train,'Text')



test = pd.read_csv('test.tsv',sep='\t',header=None)
test = format_text(test,1)




X_X = train['Text'].tolist()
Y_train = train['Label']



le = LabelEncoder()
le.fit(Y_train)
Y_train = le.transform(Y_train)


tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(X_X).toarray()


def energy(u):
# Estimate PSD `S_xx_welch` at discrete frequencies `f_welch`
    f_welch, S_xx_welch = scipy.signal.welch(u)

    # Integrate PSD over spectral bandwidth
    # to obtain signal power `P_welch`
    df_welch = f_welch[1] - f_welch[0]
    return np.sum(S_xx_welch) * df_welch



def maxvdm(f,K):
    alpha = 1      
    tau = 0.            
    #K = 4         
    DC = 0             
    init = 1           
    tol = 1e-7  
    u, u_hat, omega = VMD(f, alpha, tau, K, DC, init, tol) 
    energy_array=[]
    for i in u:
        energy_array.append(energy(i))
    ind = np.argmax(energy_array)
    return u[ind]


X_X_1 = test[1].tolist()


features_1 = tfidf.transform(X_X_1).toarray()


Y_test = le.transform(test[2])


models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LogisticRegression(random_state=0),
    KNeighborsClassifier(n_neighbors=3)
    ]


models_acc = {"RandomForestClassifier":[],"LogisticRegression":[],"KNeighborsClassifier":[]}
models_f1 = {"RandomForestClassifier":[],"LogisticRegression":[],"KNeighborsClassifier":[]}
models_pre = {"RandomForestClassifier":[],"LogisticRegression":[],"KNeighborsClassifier":[]}
models_re = {"RandomForestClassifier":[],"LogisticRegression":[],"KNeighborsClassifier":[]}

for k in range(2,11):
    print("K-Value Tuning :",k,"- out of 10")
    X_train = []
    for i in features:
        X_train.append(maxvdm(i,k))
    print("\tTraining Data Done..")
    X_test = []
    for i in features_1:
        X_test.append(maxvdm(i,k))
    print("\tTesting Data Done..")
    for i in models:
        i.fit(X_train, Y_train)
        y_pred = i.predict(X_test)
        acc = accuracy_score(Y_test, y_pred)
        f1  = f1_score(Y_test, y_pred)
        pre = precision_score(Y_test, y_pred)
        re = recall_score(Y_test, y_pred)
        name = i.__class__.__name__
        models_acc[name].append(acc)
        models_f1[name].append(f1)
        models_pre[name].append(pre)
        models_re[name].append(re)


