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



model1 = KMeans(n_clusters=13, random_state=0, init='random') 
model1.fit(X)
Y = model1.predict(X) 

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from numpy import where
Y1 =  [0,1,2,3,4]

# tsne is only used to decrease dimension for visualization
tsne = TSNE(n_components=3, init='pca', random_state=0)
x = tsne.fit_transform(X)
print(x,X)

## Visualization
plt.figure(figsize = (10,5))
plt.subplot(121)
plt.scatter(x[:,0],x[:,1],x[:,2], c = Y, 
            edgecolor = "None", alpha=0.5)
plt.colorbar()
plt.show()
