import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
path="/Users/takeidaichi/NLP/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(path, binary=True)
a=model['United_States']
b=model['US']
sum1=0
sum2=0
sum3=0
for i in range(len(a)):
    sum1+=a[i]*b[i]
    sum2+=a[i]**2
    sum3+=b[i]**2
sum2=sum2**0.5
sum3=sum3**0.5

print(sum1/(sum2*sum3))
