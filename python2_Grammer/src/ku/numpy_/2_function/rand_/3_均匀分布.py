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
范围 anywhere within the interval [a, b), and zero elsewhere.
'''
# 产生-1到0的2*2的矩阵
s = np.random.uniform(-1,0,[2,2])
print s
# 产生-1到0的有5个元素的向量
s = np.random.uniform(-1,0,5)
print s
