#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
前面四个程序是分开的组件这里把四个组件封装起来。
同时加入预处理
不加入预处理会出问题：原因不详
方便其他人调用
做成一个类，要不然cut使用不了init的数据
程序只有两个接口 
init 初始化字典
cut 切分短句


'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from a1_dict_to_preSet import load_dict
from a2_get_dag import get_DAG
from a3_get_sentence_prob import calc
from a4_cut_sentence_no_hmm import cut_max_prob_no_hmm
from a4_cut_senten_hmm import cut_max_prob_hmm
# 还要import HMM分词的类
from new_word.begin_middle_end.a4_packing import Cut_HMM   
import re


class Cut():
    # 静态变量
    # 字典文件地址
    dict_dir=r"D:\daima2\nlp\src\cut\unit_max_prob\a_sen_to_word_hmm_or_not\dict.txt"
    
    re_han = re.compile(ur"([\u4E00-\u9FD5a-zA-Z0-9+#&\._-]+)", re.U)
    re_skip = re.compile(ur"(\r\n|\s)", re.U)
    # 初始化方法
    def __init__(self,):
        # 根据字典初始化参数
        self.init(Cut.dict_dir)
        # 初始化一个cut_hmm的obj
        self.cut_hmm_obj=Cut_HMM()



    def init(self,f_dir):
        '''
        初始化字典参数
        '''
        self.pre_set, self.word_prob_dict, self.min_prob=load_dict(f_dir)
        
    
    def cut_no_hmm(self,sentence):
        '''
        no_hmm切分句子
        '''
        # 这里首先要对矩阵进行切分
        sentence = sentence.decode('utf-8')
        DAG=get_DAG(sentence,self.pre_set,self.word_prob_dict)
        route=calc(sentence, DAG, self.min_prob, self.word_prob_dict)
        cut_sen=cut_max_prob_no_hmm(sentence,route)
        return cut_sen
    

    
    def cut_hmm(self,sentence):
        '''
        hmm切分句子
        '''
        sentence = sentence.decode('utf-8')
        DAG=get_DAG(sentence,self.pre_set,self.word_prob_dict)
        route=calc(sentence, DAG, self.min_prob, self.word_prob_dict)
        cut_sen=cut_max_prob_hmm(sentence,route,self.cut_hmm_obj)
        return cut_sen
    
    def cut(self,sentence,HMM):
        if HMM:
            cut_block = self.cut_hmm
        else:
            cut_block = self.cut_no_hmm
        # 对句子进行分割    
        blocks = Cut.re_han.split(sentence)
        for blk in blocks:
            if not blk:# 如果为空
                continue
            if Cut.re_han.match(blk): # 如果满足re_han 目前能把，。过滤掉
                for word in cut_block(blk):
                    yield word
            else:
                tmp = Cut.re_skip.split(blk)# 按空白字符分割
                for x in tmp:
                    if Cut.re_skip.match(x):# 如果是空白符
                        yield x
                    else : # 一个一个输出
                        for xx in x:
                            yield xx

    
    

if __name__ == '__main__':
    sentence=u"，我叫aaa李健博"
    '''
    非HMM
    '''
    cut_obj=Cut()
    cut_sen=cut_obj.cut(sentence,True)
    for word in cut_sen:
        print word
    '''
    HMM类型
    '''
#     cut_obj=Cut()
#     cut_sen=cut_obj.cut_max_prob_hmm(sentence)
#     for word in cut_sen:
#         print word

