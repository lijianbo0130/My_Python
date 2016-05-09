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

# 这个是按顺序排，改变了尺寸的新数组，原数组的shape保持不变
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(3,2)
print a
print b
'''
[[1 2]
 [3 4]
 [5 6]]
'''
