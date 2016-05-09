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
产生正太分布的随机数
For random samples from mu 为均值 sigma 为方差
sigma * np.random.randn(...) + mu
'''
# 产生4个正太分布的  N(3, 2.5*2.5):
print 2.5 * np.random.randn(4) + 3
# 产生2*4的
print 2.5 * np.random.randn(2,4) + 3




