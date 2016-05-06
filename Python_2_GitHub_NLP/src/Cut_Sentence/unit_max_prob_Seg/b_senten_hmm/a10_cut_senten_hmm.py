#coding=utf-8
'''
Created on 2016年3月22日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
# import re
from a1_dict_to_preSet import load_dict
from a2_get_dag import get_DAG
from a3_get_sentence_prob import calc
 

'''
__cut_DAG返回精确模式 同时使用马尔科夫
调用calc得到route字典
调用get_dag得到DAG矩阵
这个函数前半部分用 calc 函数计算出了初步的分词，
而后半部分就是就是针对上面例子中未出现在语料库的词语进行分词了。
有了route字典就可以知道概率最大的一个划分
从第一个字开始 下标为x 得到y = route[x][1]+1
y为和x生成词最大概率的下标
如果为一个字用buf收集起来
如果buf搜集的一个字的长度大于1等于有多个单字无法连接成词就用
HMM函数Finalseg()去识别
x从第一个字符开始
y表示在route字典中从y到x的概率最大 
'''           
def cut_max_prob_hmm(sentence,route,chmm_obj):
    '''
    根据生成的route字典分词，分词会把字母和数字组合起来成词
    chmm_obj 是hmm_cur的对象可以调用chmm_obj 方法
    :param sentence: 需要分词的句子
    :param route: 句子的下标概率字典
    '''
#     re_eng = re.compile(ur'[a-zA-Z0-9-]',re.U)# 一个英文和数字的正则 
    x = 0
    N = len(sentence)
    buf =u''
    #从第一个开始遍历
    while x<N:
        #后面词的位置
        y = route[x][1]+1
        l_word = sentence[x:y]
        #如果是单个字符或者字
        if y-x==1:
            #用buf搜集起来  会把连续的单个字搜集起来
            buf+= l_word
            
        #如果不是单个字
        else:
            if len(buf)>0:
                #如果是字(词) 就把单个字写入
                if len(buf)==1:
                    yield buf
                    buf=u''
                else:
                #如果是字字字字 或者字符字符字符 就把多个字组合成一个词 去执行vtb算法
                    regognized = chmm_obj.clean_cut(buf)
                    for t in regognized:
                        yield t
                    buf=u''
            yield l_word        
        x =y

    if len(buf)>0:
        if len(buf)==1:
            yield buf
        else:
            regognized = chmm_obj.clean_cut(buf)
            for t in regognized:
                yield t

if __name__ == '__main__':
    sentence=u"一篇文章市场"
    '''
    pre_set 储存所有出现过的词的集合
    word_prob_dict 储存所有{词：log(概率)}的字典
    min_prob # 出现次数最少的词的log(prob)
    '''
    pre_set, word_prob_dict, min_prob=load_dict("dict.txt")
    DAG=get_DAG(sentence,pre_set,word_prob_dict)
    route=calc(sentence, DAG, min_prob, word_prob_dict)
    cut_sen=cut_max_prob_hmm(sentence,route)
    for word in cut_sen:
        print word