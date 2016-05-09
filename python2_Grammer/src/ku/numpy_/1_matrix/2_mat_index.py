#coding=utf-8
'''
Created on 2015年7月15日
@author: Administrator
'''
import numpy as np

a=np.mat([[1,2],[4,5]])

print a # [[1 2] [4 5]]
print a[0] #表示的是第一行 [[1 2]]
print a[0,1] #第一行第二个 2
print  a[:,0] # [[1] [4]]

