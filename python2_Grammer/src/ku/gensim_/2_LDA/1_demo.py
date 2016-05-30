# coding=utf-8
'''
Created on 2016年5月29日
@author: 李健博
程序作用：

'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from gensim import corpora  # 这个包是语料库包

seg_list = []
# 得到文章的分词
with open(r'seged_file.txt', 'rb') as somefile:
    for index, line in enumerate(somefile):
        lis_temp = []
        line = line.decode('utf-8')
        line = line.strip()  # 去除换行符号
        line_split = line.split("\t")  # 按照空格分开 
        for word in line_split:
            lis_temp.append(word)
        seg_list.append(lis_temp)
        

         
'''
初始化语料库包seg_list里面装的是多个list.每一个list是一个切分完的句子
如：[[w1,w2...],[w3,w1....]
dic为 一个dict{词：词的编号}
'''  
dic =corpora.Dictionary(seg_list)

for word,index in dic.token2id.iteritems():
    print word +" 编号为:"+ str(index)

