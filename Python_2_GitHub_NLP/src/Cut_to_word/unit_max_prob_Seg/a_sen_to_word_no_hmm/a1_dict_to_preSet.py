#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
把字典中的数据变成可使用的前缀树数据结构
可以使用tire_tree,但是我们并不是要查找所有以某一个词为前缀的所有词汇。
我们要查找的是所有大于二的词汇组合。
如北京大学
词典里面有 北京 大学 北京大学。
指针指到学字的时候。我们要给出。学：(默认每一字是一个词) 大学，北京大学。
所以和tire_tree还是有一定的区别。这里使用pre_set更好
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from math import log

'''
把字典文件变成可用的数据结构
'''
def load_dict(file_dir):
    '''
    这里使用的是jieba的字典
    pre_set 储存所有出现过的词的集合
    word_prob_dict 储存所有{词：log(概率)}的字典
    min_prob # 出现次数最少的词的log(prob)
    :param f_name: 字典地址
    '''
    '''
    储存所有{词：出现次数}的字典
    ｛CD机： 3,D盘 5}
    '''
    word_fre_dict = {} 
    '''
    储存所有出现过的词的集合
    如果出现 数据结构
    那么集合会加入 set(['数', '数据', '数据结', '数据结构'])
    '''
    pre_set = set() 
    #总频率 所有词出现频率相加
    sum_fre = 0.0
    with open(file_dir, 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            line_split = line.split(" ")  # 按照空格分开
            # 得到 word 和freq
            word=line_split[0]
            freq=float(line_split[1])
            word_fre_dict[word] = freq
            sum_fre += freq
            # 把所有的字加入前缀树
            # 如： 那么集合会加入 set(['数', '数据', '数据结', '数据结构'])
            for index in xrange(len(word)):
                pre_set.add(word[:index+1])
        # 把次数变成log(概率) 做归一化
        word_prob_dict,min_prob=normalize_word_fre_dict(word_fre_dict,sum_fre)
    return pre_set, word_prob_dict, min_prob

def normalize_word_fre_dict(word_fre_dict,sum_fre):
    '''
    传入进来的是储存所有{词：出现次数}的字典
    我们需要把出现次数 变成概率=出现次数/所有词出现次数相加
    同时把prob变成log形式。防止连成溢出。
    '''
    word_prob_dict = dict([(k,log(float(v)/sum_fre)) for k,v in word_fre_dict.iteritems()]) #normalize
    min_prob = min(word_prob_dict.itervalues())
    return word_prob_dict,min_prob