#coding=utf-8
from a1_dict_to_preSet import load_dict



'''
Created on 2016年3月20日
@author: 李健博
程序作用：
得到DAG图
DAG返回一个字典数据结构 key为下标 value为能和key下标组成词语的下标  
这样就有了所有可能的分词
默认单个字为一个词
Dic为
国  
国庆 
国庆节 
Sentence=国庆节国庆
DAG={0: [0, 1, 2], 1: [1], 2: [2], 3: [3, 4], 4: [4]}
0: [0, 1, 2]表示下标为0的词可以和下标为0，1，2的分别组成词组 
如 国，国庆，国庆节
返回DAG字典
'''
def get_DAG(sentence,pre_set,word_prob_dict):
    '''
    :param sentence: 需要分词的句子
    :param pre_set:储存所有出现过的词的集合
    :param word_prob_dict:储存所有{词：频率}的字典
    '''
    DAG = {}
    N = len(sentence)# 得到句子长度
    for k in xrange(N):
        '''
        储存能和当前位置k组成词组的下标
        0: [0, 1, 2] 表示当前位置k能和0,1,2三个位置成词 
        '''
        combime_list = [] 
        i = k# 得到当前位置
        frag = sentence[k]
        # 从当前位置到末尾
        while i < N and frag in pre_set:# 如果set里面有以这个字为开头的词组
            if frag in word_prob_dict:# 查看set里面的词是否在word_prob_dict中
                combime_list.append(i)# 存在证明能成词 就加入下标
            i += 1
            frag = sentence[k:i+1]
        if not combime_list:# 如果没有能和当前位置成词的词
            combime_list.append(k)# 把自己当成一个词加入
        DAG[k] = combime_list
    return DAG

if __name__ == '__main__':
    sentence=u"国庆节国庆"
    '''
    pre_set 储存所有出现过的词的集合
    word_prob_dict 储存所有{词：log(概率)}的字典
    min_prob # 出现次数最少的词的log(prob)
    '''
    
    pre_set, word_prob_dict, min_prob=load_dict("D:\daima2\DATA\src\cut_dict\jieba_dict.txt")
    DAG=get_DAG(sentence,pre_set,word_prob_dict)
    print DAG
    print "down"




