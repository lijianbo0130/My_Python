# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
读取词库的字典。
把输入的句子从前向后，用能拆分成最多的形式拆分
如：中国人民大学
会拆分成：中国 人民 大学 就算词库里面有中国人民 人民大学
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


def create_Word_Pre_Set(DictDir):
    '''
    词库只有词 不需要词频
    创建词库集合 前缀集合
    '''
    set_word = set()  # 词库字典
    set_pre = set()  # 建立前缀词典set
    with open(r'gly_new.txt', 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            word = line.strip()  # 去除换行符号
            set_word.add(word)
            for index in xrange(len(word)):
                set_pre.add(word[:index + 1])
    return set_word, set_pre
    
    
    
    def seg(DictDir, sentence):
        '''
        切分输入的句子
        :param DictDir: 字典路径
        :param sentence: 等待切分的句子
        '''
        # 得到 词库集合 前缀集合
        set_word, set_pre = create_Word_Pre_Set(DictDir)
    
    
if __name__ == '__main__':
    # 读取的词库文件名
    DictDir = "new_dict_no_duplicate.txt"  
   
    
    
             
    
            
