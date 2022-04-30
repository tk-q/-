import MeCab
import collections
import math
R=[]
mecab = MeCab.Tagger()
co=0
from collections import defaultdict
d = defaultdict(int)
d1 = defaultdict(int)
M = defaultdict(int)
n=""
count1=0
TFI=[]
num=0
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
        r1 = mecab.parse(line)
        for r in r1.split("EOS"+"\n"+"EOS"):
            if count1==0:
                count1+=1
                break
            for s in r.split("。"):
                co=0
                num+=1
                for p in s.split("\n"):
                    for t in p.split("\t"):
                        if co==0:
                            if len(t)>0 and (t!="EOS"):
                                d["BOS"+t]+=1
                                d1["BOS"+t]+=1
                                n=t
                                co+=1
                        else:
                            if len(t)>0 and (t!="EOS") and len(n)>0:
                                d[n+t]+=1
                                d1[n+t]+=1
                            if len(t)>0 and (t!="EOS"):
                                n=t
                            co+=1
                        break
                if len(n)>0:
                    d[n+"EOS"]+=1
                    d1[n+"EOS"]+=1
                n=""
                for m in d1.keys():
                    M[m]+=1
                d1 = defaultdict(int)
    
                #print(M)
                #print(d)
            for m1 in M:
                w=math.log(M[m1]+1,10)
                w1=w*math.log(num/d[m1],10)
                TFI.append(w1)
            num=0
            P1=M.keys()
            P2=TFI
            if (len(P1)!=0) and (len(P2)!=0):
                S=zip(P1,P2)
                S=sorted(S,reverse=True)
                P1,P2=zip(*S)
                num1=0
                for i in range(len(P1)):
                    print(P1[i],P2[i])
                    if num==2:
                        break
                    num+=1
            M = defaultdict(int)
            d = defaultdict(int)
            TFI=[]
            print("\n")
                
