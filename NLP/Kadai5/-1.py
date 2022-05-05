class Morph:
    def __init__(self,text):
        self.surface = text[0]
        self.base = text[8]
        self.pos = text[2]
        self.pos1 = text[2]

co=0
Cont=[]

with open('ai.ja.txt.parsed') as f:
    contents = f.read()
   
    for i in contents.split("\n"):
        s=''.join(i)
        if s[:1]=="*":
            continue
        if(s[:3]=="EOS"):
            print("\n")
            continue
        for k in i.split(","):
            for n in k.split("\t"):
                Cont.append(''.join(n))
        if len(Cont)<9:
            continue
        l=(Morph(Cont))
        print(l.surface,l.base,l.pos,l.pos1)
        Cont=[]
