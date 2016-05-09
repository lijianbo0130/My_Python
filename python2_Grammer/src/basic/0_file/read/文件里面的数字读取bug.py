#coding=utf-8
'''
Created on 2016年3月5日
@author: asus-pc
'''
from __future__ import  division

import sys

reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

with open(r'test.txt','rb') as somefile:
    for line in somefile:
        line = line.decode('utf-8')
        line= line.strip() #去除换行符号
        print line # 打印出来虽然是588 但是是一个unicode 问题是这个unicode竟然可以和数字比大小
        print type(line)# unicode
        print line>588
        num=int(line) # 读取数字要做计算的时候前面一定要加一个int
        print num # 588
        