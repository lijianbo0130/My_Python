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
model = gensim.models.Word2Vec.load_word2vec_format("out.vector", binary=False)
b=model.most_similar(u"坑爹",topn=30)
for tu in b:
    print tu[0],tu[1]

print "down"