#coding=utf-8
'''
[[2 0]
 [1 2]]
tolist 后就变成两层lis
[[2, 0], [1, 2]]
'''
import numpy as np


# mat
b=[[2,0],[1,2]]
b=np.mat(b)
print b
print b.tolist()
