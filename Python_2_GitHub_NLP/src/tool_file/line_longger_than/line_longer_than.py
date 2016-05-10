# coding=utf-8
'''
Created on 2016年5月9日
@author: 李健博
程序作用：
输出一行字数大于等于7的行
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

fileDir = "minus_5.txt"

lineLength = 5
outFileName = "bigThan"+str(lineLength)+".txt"

lis_write = []
with open(fileDir, 'rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line = line.strip()  # 去除换行符号
        if len (line) >= lineLength:
            lis_write.append(line)

with open(outFileName,'wb') as somefile:
    for line in lis_write: # 不会自动换行
        line+="\r\n"
        somefile.write(line)

print "down"

        
        


         

        
