#coding=utf-8
'''
Created on 2015年6月11日
@author: Administrator
'''
from __future__ import  division
# f.seek(0,0)   回到起始位置     
# f.seek(-12,1)  以当前位置向前移动12个字节
f = open('data.txt','w+')
f.tell()    # 0
f.write('test line l\n')      #加入一个长为12的字符串[0-11]
f.tell()    # 12
f.write('test line 2\n')      #加入一个长为12的字符串[12-23]
f.tell()    # 告诉我当前位置  24
f.seek(-12,1)                 #向后移12个字节
f.tell()    # 12
f.readline()                  # 'test line 2'
f.seek(0,0)                   # 回到最开始
f.readline()                  # 'test line 1'
f.close()
