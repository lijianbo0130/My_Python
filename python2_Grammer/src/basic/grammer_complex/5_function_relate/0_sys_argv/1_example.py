#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

import sys,os  

# sys.argv[0]表示代码本身文件路径
print sys.argv[0]
# 所以参数从1开始


if len(sys.argv) < 2:  
    print 'No action specified.'  
    sys.exit()  
# 输入 python 1_example.py a b
print sys.argv[1],sys.argv[2] # a b
# 把输入的参数按空格分割开





