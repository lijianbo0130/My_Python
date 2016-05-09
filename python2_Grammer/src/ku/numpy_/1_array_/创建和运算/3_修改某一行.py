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

# 目标 b为3*n的矩阵每一行为 x^1,x^2,x^3,x^4
a=np.array([1,2,3])
b=np.ones((3,4))
# 得到b的某一列 让它成为a的第一方
# print b[:,0] 表示第一列
for i in range(4): 
    b[:,i]=a**(i+1)
print b
