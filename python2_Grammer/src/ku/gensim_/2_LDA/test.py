#coding=utf-8
'''
Created on 2016年2月15日
@author: asus-pc
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
ducomens=[]
with open(ur'D:\daima2\DATA\src\包含武汉的新闻\分词后的格式\atricle_cut_lis.txt','rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() #去除换行符号
        word=line.split(" ")
        ducomens.append(word)
        
#     print ducomens
from gensim import corpora
from gensim import models
# 把文章变成语料的形式
dictionary = corpora.Dictionary(ducomens)
# dictionary.save('1.txt')# 保存
# print(dictionary)

# 去除不常用词
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <=100]
with open(ur'D:\daima2\DATA\src\停用词\百度停用词列表.txt','rb') as somefile:
    stop_list=[]
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() #去除换行符号
        stop_list.append(line)


id2token=dict((value,key) for key,value in dictionary.token2id.iteritems())
# print once_ids
stop_ids=[dictionary.token2id[stopword] for stopword in stop_list if stopword in dictionary.token2id]
short_ids=[tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if len(id2token[int(tokenid)])==1]
# print stop_ids
dictionary.filter_tokens(once_ids + stop_ids+short_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed

id2token=dict((value,key) for key,value in dictionary.token2id.iteritems())
# print id2token
# print(dictionary.token2id)  
'''
输出每个词和对应编号
{'minors': 11, 'graph': 10, 'system': 5, 'trees': 9, 'eps': 8, 'computer': 0,
'survey': 4, 'user': 7, 'human': 1, 'time': 6, 'interface': 2, 'response': 3}
'''
corpus = [dictionary.doc2bow(document) for document in ducomens]
# print  corpus
S=15
lda = models.ldamodel.LdaModel(corpus, num_topics=S)
print "DOWN"
for i in range(0,S):
    for tup in  lda.show_topic(i, topn=20):
        print id2token[int(tup[0])],
    print 
print "down"