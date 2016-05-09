#coding=utf-8
'''
Created on 2015年10月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


import numpy as np
'''
Create an array of the given shape and propagate it with random samples 
from a uniform distribution over [0, 1)
'''
print np.random.rand(3,2) # 3*2的矩阵
print np.random.rand(2) # 一个向量有两个元素
print np.random.rand(1,2) # 1*2的矩阵

