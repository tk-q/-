k1=int(input())
co=1
f=open("popular-names.txt")
for k in f.readlines():
    for p in k.split("\n"):
        print(p)
    if co==k1:
        break
    co+=1
