# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
读取词库的字典。
把输入的句子从后向前，用能拆分成最多的形式拆分 从后向前的效果比从前向后好
大于一个字的才会成词
如：中国人民大学
会拆分成：中国 人民 大学 就算词库里面有中国人民 人民大学
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


class MaxBackwardSeg():

    
    def __init__(self):
        # 字典地址
        self.dictDir = "new_dict_no_duplicate.txt"
        self.set_word= self.create_Word_Pre_Set()

    def create_Word_Pre_Set(self):
        '''
        词库只有词 不需要词频
        创建词库集合 
        这里的词库是从后向前的 但是 如：中国人
        存储进去还是：中国人
        '''
        set_word = set()  # 词库字典
        with open(self.dictDir, 'rb') as somefile:
            for line in somefile:
                line = line.decode('utf-8')
                word = line.strip()  # 去除换行符号
                set_word.add(word)

        return set_word
    
    
    
    def seg_backward(self, sentence):
        '''
        切分输入的句子 从前向后找
        :param DictDir: 字典路径
        :param sentence: 等待切分的句子
        从后向前找词，长度为一的跳过，继续往后找
        '''
        lis_seg_return = []  # 返回的list
        sen_len = len(sentence)  # 句子长度
        fir_index = sen_len  # 成词才移动的下标
        next_index = sen_len-1  # 每次都移动的下标
        while(next_index >= 0):
            cur_word = sentence[next_index:fir_index]  # 当前的可能的词
#             print cur_word
            # 到达最后一个字 把词加入
            if (next_index == 0):
                if (cur_word not in self.set_word):  # 不在词库中
                    if len(cur_word) == 1:  # 一个字就省略
                        pass
                    else:# 加入
                        lis_seg_return.append(cur_word)
                else:  # 在词库中
                    if len(cur_word) == 1:  # 一个字就省略
                        pass
                    else:
                        lis_seg_return.append(cur_word)
                break
            else:  # 不是最后一个字
                if cur_word not in self.set_word:  # 如果当前的字不是一个词
                    next_index -= 1
                else:
                    # 加入新词
                    if (len(cur_word)>1):  # 大于一才加入
                        lis_seg_return.append(cur_word)  
                        fir_index = next_index  
                    next_index -= 1 
        
        return lis_seg_return


                
            


    
if __name__ == '__main__':
    # 读取的词库文件名
    sentence = "龙纹身的女孩之空中城堡"
    maxSeg = MaxBackwardSeg()
    lis_seg_return = maxSeg.seg_backward(sentence)
    for word in lis_seg_return:
        print word
    


   
    
    
             
    
            
