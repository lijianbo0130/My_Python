#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''
import logging
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
#
#     program = os.path.basename(sys.argv[0])
    program="my_program"
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
#     if len(sys.argv) < 4:
#         print globals()['__doc__'] % locals()
#         sys.exit(1)
#     inp, outp1, outp2 = sys.argv[1:4]
    inp="1.txt"  # txt 文件
    outp1="out.model" # 输出文件1
    outp2="out.vector" # 输出文件2
 
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
 
    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
    print "down"