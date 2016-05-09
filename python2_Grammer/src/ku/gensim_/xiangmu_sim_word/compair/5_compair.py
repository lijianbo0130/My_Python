#coding=utf-8
'''
这个文件是查错的时候用的
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import toolkit.data as dt
from collections import OrderedDict as odic

dic_write=odic({})
with open(r'./data_in/price_word.txt','rb') as somefile:
    for line in somefile:
        word= line.strip() #去除换行符号
        word=dt.getunicode(word)
        dic_write[word]=[[],[]] # 第一个为Chinese 第二个装非chinese

import gensim

# 第一个模型
model = gensim.models.Word2Vec.load_word2vec_format("chinese_out.vector", binary=False)

for word in dic_write: 
    print word
    b=model.most_similar(word,topn=30)
    print word
    for tu in b:
        dic_write[word][0].append(tu[0]+str(tu[1])) 
  
        

        


# 第二个模型
model = gensim.models.Word2Vec.load_word2vec_format("unchinese_out.vector", binary=False)

for word in dic_write:
    try:  
        b=model.most_similar(word,topn=30)
        for tu in b:
            dic_write[word][1].append(tu[0]+str(tu[1]))  
    except:   
        dic_write[word][1]=["该词不存在于词典"]
    finally:
        pass
        


# 写入        
with open(r'./data_out/price_word_out.txt','wb') as f:
    for word in dic_write:
        f.write(word+"\n")
        f.write(" ".join(dic_write[word][0])+"\n")
        f.write(" ".join(dic_write[word][1])+"\n")
        
print "down"        
