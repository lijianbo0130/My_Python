'''
Created on 2015年2月6日
@author: asus
'''

import numpy as np

#创建矩阵
a=np.mat([[1,2,3],[4,5,6],[2,5,9]])


# 计算行列式
det=np.linalg.det(a)
print(det)
