import MeCab
import collections
R=[]
mecab = MeCab.Tagger()
co=0
from collections import defaultdict
d = defaultdict(int)
n=""
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
        r = mecab.parse(line)
        for s in r.split("。"):
            for p in s.split("\n"):
                for t in p.split("\t"):
                    
                    if co==0:
                        if len(t)>0 and (t!="EOS"):
                            d["BOS"+t]+=1
                            co+=1
                    else:
                        d[n+t]+=1
                        if len(t)>0 and (t!="EOS"):
                            n=t
                        co+=1
                    break
            d[n+"EOS"]+=1
            co=0
P1=d.values()
P2=d.keys()
S=zip(P1,P2)
S=sorted(S,reverse=True)
P1,P2=zip(*S)
for i in range(len(P1)):
    print(P1[i],P2[i])
                
