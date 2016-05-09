#coding=utf-8
'''
Created on 2015年11月22日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import numpy as np

# 减法
# 两个向量相减
a= np.array([1,2])  
b= np.array([3,4])  
print a-b # [-2 -2]

# 向量的每一个都减去一个数
print a-1 # [0 1]