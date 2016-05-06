#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
根据dag图得到最大概率的分割
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from a1_dict_to_preSet import load_dict
from a2_get_dag import get_DAG


def calc(sentence,DAG,min_prob,word_prob_dict):
    '''
    route为一个字典。
    key为字的下标，value为tuple(走到当前下标的最大概率,从哪一个下标走到当前下标)
    如：route[0]=(-32.64727553755524, 1)
    所以route[N] 的概率为log(1). 因为route[N]为下标为N+1的字，不存在所以概率为1。
    通过动态规划的方法，找到到从后向前到达每一个字的最大概率。
    如：route=
    {0: (-25.095872829519834, 2), 1: (-32.64727553755524, 1), 2: (-22.46713125055319, 2), 
    3: (-13.036438993046577, 4), 4: (-10.180144287002046, 4), 5: (0.0, '')}
    这样就知道哪一个划分概率最大
    '''
    route={}
    N = len(sentence)
    route[N] = (0.0,'')# ""为一个占位符，因为不存在一个下标到达最后一个字
#     print min_prob,"最小log(概率)"

    for idx in xrange(N-1,-1,-1): # 从句末向前移动 N-1 to 0
        # idx_list 保存所有能够走到idx点的概率
        idx_list=[]# 
        # x为能和idx组成词的下标
        for x in DAG[idx]:
            # 为下标[idx:x+1](这个词的概率)+route{x+1}[0](route｛x+1｝的累积概率)
            idx_list.append(( word_prob_dict.get(sentence[idx:x+1],min_prob) + route[x+1][0],x ))# 同时记录x
        # 去概率最大的下标作为到当前下标的路径
        route[idx] = max(idx_list)
    return route


if __name__ == '__main__':
    sentence=u"国庆节国庆"
    '''
    pre_set 储存所有出现过的词的集合
    word_prob_dict 储存所有{词：log(概率)}的字典
    min_prob # 出现次数最少的词的log(prob)
    '''
    pre_set, word_prob_dict, min_prob=load_dict("dict.txt")
    DAG=get_DAG(sentence,pre_set,word_prob_dict)
    print DAG
    route=calc(sentence, DAG, min_prob, word_prob_dict)
    print route
    print "down"
