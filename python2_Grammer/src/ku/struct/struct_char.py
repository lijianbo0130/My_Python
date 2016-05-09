#coding=utf-8
'''
Created on 2015年6月14日
@author: Administrator
'''
from __future__ import  division
import struct 

bina="1"
print struct.unpack("c", bina)# 输出  返回的是一个 tuple('1',) 
print struct.unpack("c", bina)[0]# 取第一个变量
