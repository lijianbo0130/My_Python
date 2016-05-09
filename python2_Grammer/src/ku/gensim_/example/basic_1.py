#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''

'''
打印输出日志
'''
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


'''
From Strings to Vectors
This time, let’s start from documents represented as strings:
'''
from gensim import corpora, models, similarities
'''
1_语料库
'''
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


'''
2_清洗
变成词的list [['human', 'machine', 'interface'],[ 'lab', 'abc', 'computer', 'applications']]
按空格分词 去除常见词 在stoplist中
'''
# remove common words and tokenize 去除太常见的词
stoplist = set('for a of the and to in'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]
# print texts

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

from pprint import pprint   # pretty-printer
pprint(texts)
print texts