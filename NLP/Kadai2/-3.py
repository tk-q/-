from collections import defaultdict
import math
with open('/Users/takeidaichi/NLP/neko.text.mecab', 'r') as fin:
    l=fin.read()
    co=0
    count=0
    A=[]
    co1=0
    d = defaultdict(int)
    i1=0
    co=0
    c=0
    for w in l.split("EOS\nEOS"):
        if i1==0:
            i1+=1
            continue
        for q in w.split("\n"):
            if co1==0:
                co1+=1
                continue
            for a in q.split():
                if a=="EOS" or a=="空白":
                    break
                if a=="。":
                    A=set(A)
                    for p in A:
                        d[p]+=1
                        A=[]
                    c+=1
                    break
                if a=="。":
                    break
                elif a==",":
                    break
                else:
                    A.append(a)
                break
        co+=1
        l2=d.values()
        m=d.keys()
        if len(l2)==0 and len(m)==0:
            break
        B=zip(l2,m)
        B=sorted(B)
        l2,m=zip(*B)
     
        R=len(l)
        i=0
        for l1 in l2:
            n=math.log(c/l1,10)
            print(n,m[i])
            i+=1
        print("\n")
        i=0
        co=0
        c=0
        A=[]
        l2=[]
        m=[]
        d = defaultdict(int)
    
        


