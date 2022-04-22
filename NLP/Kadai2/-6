from collections import defaultdict
import math
with open('/Users/takeidaichi/NLP/neko.text.mecab', 'r') as fin:
    l=fin.read()
    co=0
    count=0
    A=[]
    co1=0
    d = defaultdict(int)
    s = defaultdict(int)
    i1=0
    co=0
    c=0
    stack=[]
    S=[]
    nekoC=0
    for w in l.split("EOS\nEOS"):
        if i1==0:
            i1+=1
            continue
        for q in w.split("\n"):
            if co1==0:
                co1+=1
                continue
            for a in q.split():
                if a=="猫":
                    for s in S:
                        d[s]+=1
                    S=[]
                    S.append("猫")
                    nekoC=2
                elif a=="。":
                    co=0
                    nekoC=0
                    S=[]
                    break
                elif nekoC>0:
                    d[a]+=1
                    nekoC-=1
                    if nekoC==0:
                        S=[]
                elif a=="空白" or a=="EOS":
                    co=0
                    nekoC=0
                    S=[]
                    break
                else:
                    if len(S)>=2:
                        first=S.pop()
                        second=S.pop()
                        S.append(first)
                        S.append(a)
                    else:
                        S.append(a)
                break

m=d.values()      
l=d.keys()
p=zip(m,l)
p=sorted(p,reverse=True)
m,l=zip(*p)
for i in range(len(m)):
    print(m[i],l[i])
    
                    
                    
