#coding=utf-8
'''
这里介绍sin(x)函数
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import numpy as np

# 单个数字
print np.sin(0)

# 使用数组
x=[1,2,3,4,5,6]
print np.sin(x)
    