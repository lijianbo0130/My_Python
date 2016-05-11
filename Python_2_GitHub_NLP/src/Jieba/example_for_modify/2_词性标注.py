#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''
import jieba.posseg as pseg


# 函数 def cut(sentence, HMM=True):

#例子1
sen='''我爱李健博'''
words = pseg.cut(sen)
for w in words: # words 是一个 generator
    print w.word, w.flag

# 问题 因为是一个generator 不方便取到word对应的flag 解决办法
# str_flag=[]
# str_word=[]
# sen='''我爱李健博'''
# words = pseg.cut(sen)
# for w in words:
#     str_flag.append(w.flag)
#     str_word.append(w.word)
# print str_flag
# print str_word










