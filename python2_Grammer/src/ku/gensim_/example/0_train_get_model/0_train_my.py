#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''

import os.path
import sys
import multiprocessing
 
# from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
# 得到当前文件的全路径 =__file__ 表示文件的全路径
path=__file__
# 分割 得到文件夹的路径
fpath  = os.path.split(path)
# 把文件夹的路径加入系统路径 
sys.path.append(fpath)
 
if __name__ == '__main__':
    # 读取的文件 一行为一句话 词与词之间用空格分开
    inp="1.txt"  # txt 文件
    outp1="out.model" # 输出文件1
    outp2="out.vector" # 输出文件2
    # size 表示词向量的纬度 window表示用前后多少个词训练 min_count每个词至少出现多少次
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
 
    # 保存模型
    model.save(outp1)
    # 保存向量
    model.save_word2vec_format(outp2, binary=False)
    print "down"