#coding=utf-8
'''
返回非0数据的下标
'''


import numpy as np

a=[1,2,3,0,0]
#0表示行
b=np.nonzero(a)
print b# (array([0, 1, 2]),)
print b[0]# [0 1 2]

#返回二维数组非0的下标 第一个参数为行  第二个参数为列
x = [[1,2],[3,0]]
b=np.nonzero(x)
print b # (array([0, 0, 1]), array([0, 1, 0]))
for i in b:
    print i # [0 1 0]

#通常用法  返回元素中大于3的下标
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.nonzero(a>3)
print(b)
