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
    
    for w in l.split("EOS\nEOS"):
        count+=1
        #if count==4:
            #print(w)
            #break
            
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
                    break
                elif a==",":
                    break
                else:
                    A.append(a)
                break
        I=A
        A=set(A)
        for p in A:
            d[p]+=1
            A=[]
        for p in I:
            s[p]+=1
            c+=1
    
       
    co+=1
    l2=d.values()
    m=d.keys()
    if len(l2)==0 and len(m)==0:
        exit()
    B=zip(l2,m)
    B=sorted(B)
    l2,m=zip(*B)
    R=len(l)
    #for i in range(len(l2)):
        #print(l2[i],m[i])
    i=0
    N1=[]
    #print(l2)
    for l1 in l2:
        n=math.log(count/l1,10)
        n=math.log(s[m[i]]+1,10)*n
        N1.append(n)
        n=0
        i+=1
    L=zip(N1,m)
    L=sorted(L,reverse=True)
    N1,m=zip(*L)
    i=0
    for N in N1:
        print(N,m[i])
        i+=1
        #if i==3:
            #break
    
    d = defaultdict(int)
    s = defaultdict(int)        

