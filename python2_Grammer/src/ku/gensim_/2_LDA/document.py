#coding=utf-8
'''
Created on 2016年2月15日
@author: asus-pc
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


def get_stop_word():
    stop_word_set=set()
    with open(ur'D:\daima2\DATA\src\停用词\百度停用词列表.txt','rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line= line.strip() #去除换行符号
            stop_word_set.add(line)
    return stop_word_set

stop_word_set=get_stop_word()
total_word_set=set()
# 得到所有的词
with open(ur'D:\daima2\DATA\src\包含武汉的新闻\分词后的格式\5000.txt','rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() #去除换行符号
        words=line.split(" ")
        for word in words:
            if word in stop_word_set:
                continue
            else:
                total_word_set.add(word)
                
total_word_list=list(total_word_set)
total_word_key={}
for index,content in enumerate(total_word_list):
    total_word_key[content]=index

total_value_key=dict((value,key) for key,value in total_word_key.iteritems())
# 做出矩阵
with open(ur'D:\daima2\DATA\src\包含武汉的新闻\分词后的格式\100.txt','rb') as somefile:
    ducumens=[]
    for line in somefile:
        ducoment=[]
        line = line.decode('utf-8')
        line= line.strip() #去除换行符号
        words=line.split(" ")
        for word in words:
            if word in stop_word_set:
                continue
            else:
                ducoment.append(total_word_key[word])
        ducumens.append(ducoment)

print ducumens[0]
from gensim import corpora, models, similarities     
dictionary = corpora.Dictionary(texts)
dictionary.save('a.txt') # store the dictionary, for future reference
print(dictionary)
     
                
                


        