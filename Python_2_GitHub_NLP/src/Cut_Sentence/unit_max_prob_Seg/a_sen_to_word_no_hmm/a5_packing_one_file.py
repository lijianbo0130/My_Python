#coding=utf-8
'''
Created on 2016年3月23日
@author: 李健博
程序作用：
把所有的文件集合到一个文件里面
非hmm新词识别
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from math import log
import re

class Cut_Sentence():

    # 字典文件地址
    dict_dir=r"D:\daima2\DATA\src\cut_dict\jieba_dict.txt"
    # 一个英文和数字的正则 分词的时候会把单个的英语和数字连起来
    re_eng_dig = re.compile(ur'[a-zA-Z0-9-]',re.U)
    
    def __init__(self,):
        # 根据字典初始化参数
        self.pre_set, self.word_prob_dict, self.min_prob=self.load_dict(Cut_Sentence.dict_dir)
        
    def get_DAG(self,sentence,pre_set,word_prob_dict):
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
    
    def calc(self,sentence,DAG,min_prob,word_prob_dict):
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
        
    def cut_no_hmm(self,sentence):
        '''
        no_hmm切分句子
        '''
        # 这里首先要对矩阵进行切分
        sentence = sentence.decode('utf-8')
        DAG=self.get_DAG(sentence,self.pre_set,self.word_prob_dict)
        route=self.calc(sentence, DAG, self.min_prob, self.word_prob_dict)
        cut_sen=self.cut_max_prob_no_hmm(sentence,route)
        return cut_sen
    def cut_max_prob_no_hmm(self,sentence,route):
        '''
        根据生成的route字典分词，分词会把字母和数字组合起来成词
        :param sentence: 需要分词的句子
        :param route: 句子的下标概率字典
        '''
         
        x = 0
        N = len(sentence)
        buf = u''
        while x<N:
            # route[x]为元组 第一个概率 第二个是到当前位置概率最大的下标 y为到达
            y = route[x][1]+1
            # 得到从后向前的概率最大的词
            l_word = sentence[x:y] # 因为list[x,y]实际上输出的是x,x+1..y-1
            # 如果是0-9 a-z    实际上是把数字和字符存放进buf里面 知道下一个不是数字和字符把buf整个输出
            if Cut_Sentence.re_eng_dig.match(l_word) and len(l_word)==1:
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

    
    def load_dict(self,file_dir):
        '''
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
        with open(file_dir, 'rb') as f:
            #行数
            linenum = 0
            for line in f.read().rstrip().decode('utf-8').split('\n'):
                linenum += 1
                #得到 word 和freq
                word,freq = line.split(' ')[:2]
                freq = float(freq)
                word_fre_dict[word] = freq
                sum_fre += freq
                for ch in xrange(len(word)):
                    pre_set.add(word[:ch+1])
            # 把次数变成log(概率) 做归一化
            word_prob_dict,min_prob=self.normalize_word_fre_dict(word_fre_dict,sum_fre)
        return pre_set, word_prob_dict, min_prob
    
    def normalize_word_fre_dict(self,word_fre_dict,sum_fre):
        '''
        传入进来的是储存所有{词：出现次数}的字典
        我们需要把出现次数 变成概率=出现次数/所有词出现次数相加
        同时把prob变成log形式。防止连成溢出。
        '''
        word_prob_dict = dict([(k,log(float(v)/sum_fre)) for k,v in word_fre_dict.iteritems()]) #normalize
        min_prob = min(word_prob_dict.itervalues())
        return word_prob_dict,min_prob
    
if __name__ == '__main__':
    '''
    这里把前面的函数拼接成一个类
    里面有一个正则
    # 一个英文和数字的正则 分词的时候会把单个的英语和数字连起来
    '''
    sen=u"一篇市场文章"
    # 创建一个对象
    cs=Cut_Sentence()
    # 切分句子 返回一个list
    word_lis=cs.cut_no_hmm(sen)
    for word in word_lis:
        print word
        