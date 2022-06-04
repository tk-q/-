from collections import defaultdict
import numpy as np

math    = [6, 4, 5, 10, 2, 8, 3, 9, 1, 7]
english = [10, 1, 4, 9, 3, 8, 6, 5, 2, 7]

def spearman(math, english):
    math = np.array(math)
    english = np.array(english)
    N = len(math)

    return 1 - (6*sum((math -english)**2) / (N*(N**2 - 1)))
co=0
number=[]
d = defaultdict(list)

spearman(math ,english) #0.6727272727272727
f=open('Vec_BCCWJ_w2v_all_win10_dim300_skipgram_ns5.txt')
with open('Vec_BCCWJ_w2v_all_win10_dim300_skipgram_ns5.txt', 'r') as fin:
    for line in fin.readlines():
        co+=1
        if co>=2:
          
            co1=0
            
            for l in line.split(" "):
                q=co1
                if co1>0:
                    if co1==1:
                        m=np.array([l])
                    else:
                        if not l=="\n":
                            m=np.append(m,l)
                co1+=1
            co1=0
            d[q].append(m)
    
print(d)
