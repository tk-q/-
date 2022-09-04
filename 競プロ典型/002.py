N=int(input())
import itertools
count1=0
count2=0
M=[]
M1=set()
m=""
co3=0
Flag=True
if N%2==0:
    for k in range(2**N):
        for l in range(N):
            if ((k>>l)&1)==1:
                m+=")"
                count1+=1
            else:
                m+="("
                count2+=1
            if count2>count1 or count2>N//2 or count1>N//2:
                count1=0
                count2=0
                m=""
                Flag=False
                break
        if Flag==True:
            print(m[::-1])
            co3+=1
        m=""
        Flag=True

