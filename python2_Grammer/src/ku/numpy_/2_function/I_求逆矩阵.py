#coding=utf-8
'''
Created on 2015年2月6日
@author: asus
'''

import numpy as np

#创建矩阵
a=np.mat([[1,2,3],[4,5,6],[2,5,9]])

#求逆矩阵
b=a.I
print(b)
c=a*b 
print(c)# 为单位矩阵


