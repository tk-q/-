import queue
k1=int(input())
co=1
q = queue.Queue()
f=open("popular-names.txt")
for k in f.readlines():
    for p in k.split("\n"):
        q.put(p)
    if co>k1:
        q.get()
    co+=1
    print(q)
print(q)
