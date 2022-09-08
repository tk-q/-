import collections
def top3(sentence,score):
    
    Flag=False
    score1=sorted(score,reverse=True)
    sum1=0
    score_limit=score1[5]
    
    for i in range(len(score1)):
        if score_limit==score[i]:
            l=sentence[i]
            
        if i+1>len(sentence):
            break
        if sentence[i]==" ":
            break
        if score[i]>=score_limit:
            print(score[i],sentence[i]+"。")
    sum1=0
    print("------------------------------------------------------------------------------------------------------------")
    print("✨",str(score_limit),l)
    print("============================================================================================================")
       
            
import MeCab
co=0
from collections import defaultdict
import math
import re
from collections import defaultdict
lineterm = defaultdict(int) #idfを計算するため

sentence=[]
with open('/Users/takeidaichi/toshishun.txt', 'r',encoding="shift_jis") as fin:
    l=fin.read()
    tagger = MeCab.Tagger("-Owakati")
#前処理
    # ヘッダの除去
    #l = re.split('\-{5,}',l)[2]
    # フッタの除去
    #l = re.split('底本：',l)[0]
    # 最初の一の除去
    
    # ふりがなの削除
    l = re.sub('《.+?》', '', l)
    # 入力注の削除
    l = re.sub('［＃.+?］','',l)
    
    # 空行の削除
    l = l.split('\n\n')
    l2=""
    l3=[]
    for w in l:
        if len(str(w))==1:
            l3.append(l2)
            l2=""
        else:
            
            l2+=w
    if len(l2)>1:
        l3.append(l2)
    l=l3
   
        
            
    for i in range(len(l)):
        print(str(i+1)+"章")
        co=0
        term_freq=[]
        for txt in l[i].split("。"):
            co+=1
            
            words = tagger.parse(txt).split('\n')[:]
            
            #値を入れていくdict
            wordFreq = {}
            sen=""
            #各行の全単語を処理するまで繰り返し
            for word in words:
                
                for l1 in word.split(" "):
                    if l1==" " or l1=="\u3000":
                        continue
                    sen+=str(l1)
                    #既出の単語なら1を足す、なければ1を入れる。
                    if l1 in wordFreq:
                        wordFreq[l1] += 1
                    else:
                        wordFreq[l1] = 1
            sentence.append(sen)
            sen=""
            term_freq.append(wordFreq)
            
            #集計した単語の,出現回数を出力、行に何がいくつあるのか
            for term, count in wordFreq.items():
                
                lineterm[term]+=1
            score=[]
            sum1=0
            count=0
        for t1 in range(co):
            for WORD,num in term_freq[t1].items():
                sum1+=num*(1/lineterm[WORD])
                    #num 
                count+=1
            score.append(sum1/count)
        sentence=sentence[:-1]
        score=score[:-1]
        top3(sentence,score)
        sentence=[]
        score=[]
        
        lineterm = defaultdict(int) 
                
    
    
