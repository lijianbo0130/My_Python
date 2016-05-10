# coding=utf-8
'''
Created on 2016年5月9日
@author: 李健博
程序作用：
从bigFile中删除smallFile中出现的行
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


bigFile="minus_4.txt"
smallFile="1.txt"
newFile="minus_5.txt"

lis_write=[]
with open(bigFile,'rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() # 去除换行符号
        lis_write.append(line)
        
smallSet=set()
with open(smallFile,'rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() # 去除换行符号
        smallSet.add(line)

with open(newFile,'wb') as somefile:
    for line in lis_write: # 不会自动换行
        if line not in smallSet:
            line+="\r\n"
            somefile.write(line)
print "down"
        


         

        
        
        


         

        