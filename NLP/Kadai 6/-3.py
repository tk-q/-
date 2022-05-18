from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
X=[]
Y=[]
co=0

import numpy as np
X1=np.array(X)
Y=np.array(Y)
f1=open('resu1.txt')
key=f1.read()
K={}
co1=0
for w in key.split(","):
     for w1 in w.split("{"):
          for w2 in w1.split("}"):
               for w3 in w2.split("'"):
                    for w4 in w3.split("'"):
                         for w5 in w4.split(" "):
                              K[w5]=co1
     co1+=1
P=[0]*18220
new=0
s2=0
l=0
num=0
with open('resu.txt') as f:
    contents = f.read()
    for i in contents.split("\n"):
        #print(i)
        num+=1
        co=0
        for s in i.split("\t"):
            s2=s.split(" ")
            if new==0:
                new+=1
                continue
            for s1 in s2: 
                
                if co==0:
                    #if new!=0:
                    if l>0:
                        
                        Y=np.append(Y,P)
                       
                        #new+=1
                        
                        P=[0]*18220
                    if s2[0]=="0":
                        X1=np.append(X1,0)
                    else:
                        X1=np.append(X1,1)
                       
                else:
                    
                        #print(s1)
                        #print(K[s])
                  
                    if s1 in K.keys():
                        l+=1
                        
                        m=K[s1]
     
                        P[int(m)]+=1
                co+=1
#Y=np.array(Y,P)
#X1=X1.reshape(1,-1)
Y=np.append(Y,P)
S=len(Y)//18220
Y=Y.reshape(S,18220)
print(X1)
print(Y)
print(len(X1),len(Y))
clf = LogisticRegression().fit(Y,X1) # x,y のペアで学習


