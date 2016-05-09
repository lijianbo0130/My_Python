#coding=utf-8
'''
Created on 2015年8月24日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
python 默认的float小数点位数是有限制的
但是用decimal包可以解决这个问题 指定任意位数的小数
decimal 为系统自带包
'''
a=0.123456789123456789
print a #0.123456789123  12位小数



