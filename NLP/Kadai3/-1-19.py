co=1
L=[]
import collections

f=open("popular-names.txt")
for k in f.readlines():
    for p in k.split("\n"):
        for k in p.split("\t"):
            if k!='':
                L.append(k)
            break
        co+=1
c = collections.Counter(L)
P1=c.values()
P2=c.keys()
S=zip(P1,P2)
S=sorted(S,reverse=True)
P1,P2=zip(*S)
for i in range(len(P1)):
    print(P1[i],P2[i])
