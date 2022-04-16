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
               co=0
               break
c = collections.Counter(R)       
print(c)
