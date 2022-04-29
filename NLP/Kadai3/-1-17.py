co=1
L=[]
f=open("popular-names.txt")
for k in f.readlines():
    for p in k.split("\n"):
        for k in p.split("\t"):
            if k!='':
                L.append(k)
            break
        co+=1
print(set(L))
