
k1=int(input())
co=1
F=[[]*1000 for i in range(k1)]
f=open("popular-names.txt")
for k in f.readlines():
    for p in k.split("\n"):
        l=co%k1
        for m in p:
            if "A"<=m and m<="Z":
                F[l].append(p)
                break
        co+=1
for i in range(k1):
    for n in F[i]:
        print(n)
        #print("\n")
    print("\n")
    print("\n")

       
