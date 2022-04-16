import MeCab
mecab = MeCab.Tagger()
co=0
f = open('neko.text.mecab', 'w')
with open('/Users/takeidaichi/Library/Mobile Documents/com~apple~CloudDocs/大学院　授業/自然言語処理/neko.txt', 'r') as fin:
    for line in fin.readlines():
       r = mecab.parse(line)
       f.write(r)
f.close()
