import MeCab
import collections
mecab = MeCab.Tagger()
from collections import defaultdict

def w():
    R=[]
    co=0
    from collections import defaultdict
  
    n=""
    with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
        for line in fin.readlines():
            r = mecab.parse(line)
            for s in r.split("。"):
                for p in s.split("\n"):
                    for t in p.split("\t"):
                        q1[t]+=1
                        if co==0:
                            if len(t)>0 and (t!="EOS"):
                                co+=1
                        else:
                            if len(t)>0 and (t!="EOS"):
                                n=t
                            co+=1
                        break
                co=0
                q1["BOS"]+=1
    return q1

d = defaultdict(int)
q１=defaultdict(int)
n=""
co=0
R=[]
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
        r = mecab.parse(line)
        for s in r.split("。"):
            for p in s.split("\n"):
                for t in p.split("\t"):
                    
                    if co==0:
                        if len(t)>0 and (t!="EOS"):
                            d["BOS"+"/"+t]+=1
                            co+=1
                    else:
                        d[n+"/"+t]+=1
                        if len(t)>0 and (t!="EOS"):
                            n=t
                        co+=1
                    break
            d[n+"/"+"EOS"]+=1
            co=0
P1=list(d.values())
P2=list(d.keys())
N=len(P1)
S3=w()
S1=len(S)
for i in range(len(P1)):
    i1=P2[i].split('/')
    print(i1)
    P1[i]=(P1[i]+1)/(S3[i1[0]]+S1)
    break
S=zip(P1,P2)
S=sorted(S,reverse=True)
P1,P2=zip(*S)
k = defaultdict(int)
for i in range(len(P1)):
    k[P2[i]]=P1[i]
print((k["BOS/吾輩"]/q1["BOS"])*
      (k["吾輩/は"]/q1["吾輩"])*
      (k["は/猫"]/q1["は"])*
      (k["猫/で"]/q1["猫"])*
      (k["で/は"]/q1["で"])*
      (k["は/ない"]/q1["は"])*
      (k["ない/EOS"]/q1["ない"])
     )

print((k["BOS/名前"]/q1["BOS"])*
      (k["名前/は"]/q1["名前"])*
      (k["は/まだ"]/q1["は"])*
      (k["まだ/ない"]/q1["まだ"])*
      (k["ない/EOS"]/q1["ない"])
     )
print((k["BOS/吾輩"]/q1["BOS"])*
      (k["吾輩/は"]/q1["吾輩"])*
      (k["は/犬"]/q1["は"])*
      (k["犬/で"]/q1["犬"])*
      (k["で/ある"]/q1["で"])*
      (k["ある/EOS"]/q1["ある"])
     )
