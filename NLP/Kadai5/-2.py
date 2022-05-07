from collections import defaultdict
class Morph:
    def __init__(self,text):
        self.surface = text[0]
        self.base = text[7]
        self.pos = text[1]
        self.pos1 = text[2]

class Chunk:
    def __init__(self,morphs,dst):
        self.morphs =morphs
        self.dst = dst
        self.srcs =[]
        self.phrase = ''.join([morph.surface for morph in morphs])

co=0
Cont=[]
co1=0
co2=0
word=[]
q=0
q1=0
K=[]*50
L1=[]*50
word1=[]
word2=[]
word3=[]
dict = defaultdict(list)
pq=0
with open('ai.ja.txt.parsed') as f:
    contents = f.read()
    for i in contents.split("\n"):
        co2+=1
        co1+=1
        
    
        if i[:1]=="*":
            #print(q1,"dst「"+str(q)+"」",''.join(word))
            word1.append(''.join(word)) #文節
            word2.append(q)#どこに係るか
            word3.append(q1)#何番目の文節か
            dict[int(q)].append(q1)
            word=[]
            for d in i.split(" "):
                co1+=1
                if co1==4:
                    q=d[:-1:]
                    
                    
                if co1==3:
                    q1=d
                    if q1=='0':
                        if pq!=0:   
                            for s1 in range(len(word1)):
                                print("["+str(word3[s1])+"]",str(word1[s1]) ,":"+str(dict[s1]))
                                #print(dict)
                            dict=defaultdict(list)
                            word1=[]
                            word2=[]
                            word3=[]
                        pq+=1
                
                
        else:
             for d in i.split("\t"):
                 word.append(d)
                 break
           
        co1=0
        s=''.join(i)
        #print(s)
        if s[:1]=="*":
            continue
        if(s[:3]=="EOS"):
            #print("\n")
            continue
        for k in i.split(","):
            for n in k.split("\t"):
                Cont.append(''.join(n))
        if len(Cont)<9:
            continue
        #l=(Chunk(Cont))
        #print(l.c)
        Cont=[]
#word1.append(''.join(word))
#word2.append(q)
#word3.append(q1)
#print(''.join(word),q,q1)
    #for s1 in range(len(word1)):
        #print(word1[s1],word2[s1],word3[s1])
   
    
    
