import MeCab
import collections
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame
R=[]
mecab = MeCab.Tagger()
co=0
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
       r = mecab.parse(line)
       for k in r.split():
           co+=1
           if co==4:
               R.append(k)
               co=0
               break
c = collections.Counter(R)
A=c.values()
A=sorted(A,reverse=True)
B=c.keys()
C=[]
for i in range(len(A)):
    C.append(i)
plt.plot(C,A)
