import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
path="/Users/takeidaichi/NLP/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(path, binary=True)
S=len(model)
k=model['Spain']-model['Madrid']+model['Athens']
print(k)
model['newq']=k
from pprint import pprint
pprint(model.most_similar('newq', topn=20))
