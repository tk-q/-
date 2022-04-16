import MeCab
import collections
R=[]
mecab = MeCab.Tagger()
co=0
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
       r = mecab.parse(line)
       for k in r.split():
           co+=1
           if co==4:
               R.append(k)
           if co==5:
               if k[0:2]!="名詞":
                   R.pop()
               co=0
               break
c = collections.Counter(R)       
print(c)
