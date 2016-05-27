# coding=utf-8
'''
Created on 2016年5月16日
@author: 李健博
程序作用：
把标书拆分成短句
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from Cut_to_sen.cut_to_sen import Cut_to_sen

# 分割句子的对象
cut_to_sen=Cut_to_sen()
lis_write=[]
with open(r'text6000000_6010000.txt','rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() # 去除换行符号
        line_split =line.split("\t")# 按照空格分开 
        article=line_split[1]
        sens=cut_to_sen.cut_article(article)
        for sen in sens:
            lis_write.append(sen.strip())
            
with open(r'biaoshu_short_sen.txt','wb') as somefile:
    for line in lis_write: # 不会自动换行
        line+="\r\n"
        somefile.write(line)

print "down"
            

        


         

        