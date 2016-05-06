#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
把一个句子拆分输出最大概率分词
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re
from a1_dict_to_preSet import load_dict
from a2_get_dag import get_DAG
from a3_get_sentence_prob import calc


def cut_max_prob_no_hmm(sentence,route):
    '''
    根据生成的route字典分词，分词会把字母和数字组合起来成词
    :param sentence: 需要分词的句子
    :param route: 句子的下标概率字典
    '''
    re_eng = re.compile(ur'[a-zA-Z0-9-]',re.U)# 一个英文和数字的正则 
    x = 0
    N = len(sentence)
    buf = u''
    while x<N:
        # route[x]为元组 第一个概率 第二个是到当前位置概率最大的下标 y为到达
        y = route[x][1]+1
        # 得到从后向前的概率最大的词
        l_word = sentence[x:y] # 因为list[x,y]实际上输出的是x,x+1..y-1
        # 如果是0-9 a-z    实际上是把数字和字符存放进buf里面 知道下一个不是数字和字符把buf整个输出
        if re_eng.match(l_word) and len(l_word)==1:
            buf += l_word
            x =y
        else:
            # 如果不是就返回以前的buf 然后返回现在的词
            if len(buf)>0:
                yield buf
                buf = u''
            yield l_word
            x =y
    #如果最后的是0-9 a-z 还是要返回
    if len(buf)>0:
        yield buf
        buf = u''

if __name__ == '__main__':
    sentence=u"一篇文章市场"
    '''
    pre_set 储存所有出现过的词的集合
    word_prob_dict 储存所有{词：log(概率)}的字典
    min_prob # 出现次数最少的词的log(prob)
    '''
    # 初始化字典
    pre_set, word_prob_dict, min_prob=load_dict(r"D:\daima2\DATA\src\cut_dict\jieba_dict.txt")
    # 得到有向图
    DAG=get_DAG(sentence,pre_set,word_prob_dict)
    # 得到图的概率
    route=calc(sentence, DAG, min_prob, word_prob_dict)
    # 由概率得到分词
    cut_sen=cut_max_prob_no_hmm(sentence,route)
    for word in cut_sen:
        print word