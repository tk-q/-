A=[]
B=[]
f = open('cal1.txt', 'a')
p = open('cal2.txt', 'a')
with open('/Users/takeidaichi/NLP/popular-names.txt', 'r') as fin:
    for line in fin.readlines():
        co=0
        for k in line.split("\t"):
            if co==2:
                f.write(k)
                f.write("\n")
            elif co==3:
                p.write(k)
            co+=1
f.close()
p.close()
fin.close()
