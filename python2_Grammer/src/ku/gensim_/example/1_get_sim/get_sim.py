#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

import gensim
# 载入刚刚训练后的vector文件
model = gensim.models.Word2Vec.load_word2vec_format("out.vector", binary=False)
# 得到和一个词的最相似的词语  一个参数为词 第二个参数为需要top多少
lis_word=model.most_similar(u"性价比",topn=30)
for tu in lis_word: # b为一个list tu为tuple类型  第一个为词 第二个为相似度 
    print tu[0],tu[1]

print "down"