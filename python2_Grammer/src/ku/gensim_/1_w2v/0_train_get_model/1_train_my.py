#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''

import logging
import multiprocessing
import os.path
import sys

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':
    '''
    日志记录不要删除，可以看见执行的过程
    '''
    program="my_program"
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    '''
    读取的文件 一行为一句话 词与词之间用(空格或者tab)分开
    '''
    inp="forword2vec.txt"  # txt 文件
    outp1="out.model" # 输出文件1
    outp2="out.vector" # 输出文件2
    '''
    size 表示词向量的纬度 window表示用前后多少个词训练 min_count每个词至少出现多少次
    '''
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
 
    # 保存模型
    model.save(outp1)
    # 保存向量 向量可以用来得到相似的词
    model.save_word2vec_format(outp2, binary=False)
    print "down"