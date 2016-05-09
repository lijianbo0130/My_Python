# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
读取词库的字典。
把输入的句子从前向后，用能拆分成最多的形式拆分
大于一个字的才会成词
如：中国人民大学
会拆分成：中国 人民 大学 就算词库里面有中国人民 人民大学
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


class MaxSeg():

    
    def __init__(self):
        # 字典地址
        self.dictDir = "new_dict_no_duplicate.txt"
        self.set_word, self.set_pre = self.create_Word_Pre_Set()

    def create_Word_Pre_Set(self):
        '''
        词库只有词 不需要词频
        创建词库集合 前缀集合
        '''
        set_word = set()  # 词库字典
        set_pre = set()  # 建立前缀词典set
        with open(self.dictDir, 'rb') as somefile:
            for line in somefile:
                line = line.decode('utf-8')
                word = line.strip()  # 去除换行符号
                set_word.add(word)
                for index in xrange(len(word)):
                    set_pre.add(word[:index + 1])
        return set_word, set_pre
    
    
    
    def seg_forward(self, sentence):
        '''
        切分输入的句子 从前向后找
        :param DictDir: 字典路径
        :param sentence: 等待切分的句子
        从前向后找词，长度唯一的跳过，继续往后找
        '''
        lis_seg_return = []  # 返回的list
        sen_len = len(sentence)  # 句子长度
        fir_index = 0  # 第一个下标
        next_index = 0  # 每次都移动的下标
        while(next_index <= sen_len):
            cur_word = sentence[fir_index:next_index ]  # 当前的字
            # 到达最后一个字 把词加入
            if (next_index == sen_len):
                last_word=sentence[fir_index:next_index] # 最后剩下的一个词
                if (last_word not in self.set_word):# 不在词库中
                    if len(last_word)==1:# 一个字就省略
                        pass
                    else:
                        lis_seg_return.append(last_word)
                else: # 在词库中
                    if len(last_word)==1:# 一个字就省略
                        pass
                    else:
                        lis_seg_return.append(last_word)
                break
            else:  # 不是最后一个字
                if cur_word not in self.set_word:  # 如果当前的字不是一个词
                    next_index += 1
                else:
                    # 加入新词
                    if (next_index - fir_index > 1):  # 大于一才加入
                        lis_seg_return.append(sentence[fir_index:next_index])  
                        fir_index = next_index  
                    next_index += 1 
        
        return lis_seg_return

#     def seg_backward(DictDir, sentence):
#         '''
#         切分输入的句子 从后向前找
#         :param DictDir: 字典路径
#         :param sentence: 等待切分的句子
#         '''
#         # 得到 词库集合 前缀集合 目前前缀词好像没用
#         set_word, set_pre = create_Word_Pre_Set(DictDir)
#         lis_seg_return = []  # 返回的list
#         sen_len = len(sentence)  # 句子长度
#         fir_index = sen_len  # 第一个下标
#         next_index = sen_len  # 每次都移动的下标
#         while(next_index >=0):
#             cur_word = sentence[next_index:fir_index ]  # 当前的字
#             # 到达最后一个字 把词加入
#             if (next_index == 0):
#                 lis_seg_return.append(sentence[next_index:fir_index])
#                 # 如果最后一个词 在不在 词库中 在末尾加个flag标识
#                 if sentence[fir_index:next_index] not in set_word:
#                     lis_seg_return.append("false")
#                 else:
#                     lis_seg_return.append("true")
#                 break
#             else:  # 不是最后一个字
#                 if cur_word not in set_word:  # 如果当前的字不是一个词
#                     next_index -= 1
#                 else:
#                     # 加入新词
#                     if (next_index-fir_index>1):
#                         lis_seg_return.append(cur_word)  
#                         fir_index = next_index  
#                     next_index -= 1 
#         
#         return lis_seg_return
                
            


    
if __name__ == '__main__':
    # 读取的词库文件名
    sentence = "龟山电视塔"
    maxSeg = MaxSeg()
    lis_seg_return = maxSeg.seg_forward( sentence)
    for word in lis_seg_return:
        print word
    

   
    
    
             
    
            
