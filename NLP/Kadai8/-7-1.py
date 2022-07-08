co=0
country=[]
l2=""
with open('/Users/takeidaichi/NLP/Kadai8-7-1.txt') as file_in:
    for line in file_in:
        if co<=1:
            co+=1
            continue
        else:
            k=0
            for s in line.split(","):
                k+=1
                if k==3:
                    break
                if k==2:
                    s=s.replace('"','')
                    s=s.replace(" ","_")
                    country.append(s)
                    
from gensim.models import KeyedVectors
path="/Users/takeidaichi/NLP/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(path, binary=True)
print(type(model))

X=[]
Y=[]
for C in country:
    if C in model:
        X.append(model[C])
        Y.append(C)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

model1 = KMeans(n_clusters=5, random_state=0, init='random')  # initを省略すると、k-means++法が適応される(randomではk-means法が適応)
model1.fit(X)
clusters = model1.predict(X)  # データが属するクラスターのラベルを取得
print(clusters)

# model.cluster_centers_ でクラスター重心の座標を取得できる

