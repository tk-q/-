co=0
co1=0
with open('sentiment.txt') as f:
    contents = f.read()
    for i1 in contents.split("\n"):
        for i in i1.split("\t"):
            print(i)
            if i=="1":
                co+=1
            else:
                co1+=1
            break
print("正:",co)
print("負:",co1)
