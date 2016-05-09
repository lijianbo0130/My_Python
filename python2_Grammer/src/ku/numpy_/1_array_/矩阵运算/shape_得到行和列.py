#coding=utf-8
'''
得到数组的长度
'''
import numpy as np

#得到数组的长度
a=np.array([[1,1],[2,2],[2,2]])
print np.shape(a) # (3, 2)


#得到某一维的长度  [0]表示有多少行 [1]表示有多少列
print(a.shape[0])
print(a.shape[1])