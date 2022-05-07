f=open('neg.txt',mode='w')
P=[]
with open('rt-polaritydata/rt-polarity.neg',encoding='latin1') as fin:
    for line in fin.readlines():
        for k in line.split("\n"):
            if len(k)>0:
                P.append(str(1)+'\t'+str(k)+'\n')
            
with open('rt-polaritydata/rt-polarity.pos',encoding='latin1') as fin:
    for line in fin.readlines():
        for k in line.split("\n"):
            if len(k)>0:
                P.append(str(0)+'\t'+str(k))
print(P)
import random
M=[]
for i in range(len(P)):
    M.append(i)
random.shuffle(M)

print(P)
for s in M:
    f.write(P[s]+'\n')
f.close()
fin.close()
