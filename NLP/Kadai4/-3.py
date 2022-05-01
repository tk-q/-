import MeCab
import collections
R=[]
q１ = defaultdict(int)
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
                    q1[t]+=1
                    
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
            q1["BOS"]+=1
P1=d.values()
P2=d.keys()
S=zip(P1,P2)
S=sorted(S,reverse=True)
P1,P2=zip(*S)
k = defaultdict(int)
for i in range(len(P1)):
    k[P2[i]]=P1[i]
W=Me()
print((k["BOS吾輩"]/q1["BOS"])*
      (k["吾輩は"]/q1["吾輩"])*
      (k["は猫"]/q1["は"])*
      (k["猫で"]/q1["猫"])*
      (k["では"]/q1["で"])*
      (k["はない"]/q1["は"])*
      (k["ないEOS"]/q1["ない"])
     )

print((k["BOS名前"]/q1["BOS"])*
      (k["名前は"]/q1["名前"])*
      (k["はまだ"]/q1["は"])*
      (k["まだない"]/q1["まだ"])*
      (k["ないEOS"]/q1["ない"])
     )
print((k["BOS吾輩"]/q1["BOS"])*
      (k["吾輩は"]/q1["吾輩"])*
      (k["は犬"]/q1["は"])*
      (k["犬で"]/q1["犬"])*
      (k["である"]/q1["で"])*
      (k["あるEOS"]/q1["ある"])
     )

