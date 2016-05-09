#coding=utf-8
'''
全部是1的数组
'''

import numpy as np 
#2*2的矩阵
a=np.ones((2,2))
print(a)# [[ 1.  1.] [ 1.  1.]]

#一纬
a=np.ones(5)
print(a)# [ 1.  1.  1.  1.  1.]

#不仅仅是1还可以是其他的
D=np.mat(np.ones((2,1))/6)
print(D)# [[ 0.16666667] [ 0.16666667]]
