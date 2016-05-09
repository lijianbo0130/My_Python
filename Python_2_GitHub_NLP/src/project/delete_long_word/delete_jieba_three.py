# coding=utf-8
'''
Created on 2016年5月9日
@author: 李健博
程序作用：
用jieba词库拆分 如果有大于三的词提取出来
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import jieba


lis_write = []
with open(r'minus_3.txt', 'rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line = line.strip()  # 去除换行符号
        seg_generator = jieba.cut(line, cut_all=False, HMM=True)
        seg_lis = list(seg_generator)
        if len(seg_lis) >= 3:
            lis_write.append(line)

with open(r'1.txt','wb') as somefile:
    for line in lis_write: # 不会自动换行
        line+="\r\n"
        somefile.write(line)
print "down"


        
        


         

        
