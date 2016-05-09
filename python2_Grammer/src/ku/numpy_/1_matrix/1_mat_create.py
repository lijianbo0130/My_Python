#coding=utf-8
'''
创建矩阵
'''

import numpy as np

#创建矩阵
#方法一
# a=np.mat([[1,2],[4,5]])
# print(a) # [[1 2] [4 5]]

#方法二
# b=[[1,2],[4,5]]
# b=np.mat(b)
# print(b)# [[1 2] [4 5]]

#不管怎么样都会有两个[[]]
# b=[1,2,3]
# print np.mat(b)# [[1 2 3]]

# print np.mat(1) # [[1]]

# 一个元素 用tolist没什么用
# a=np.mat(1)
# print type(a)
# b=a.tolist()
# print type(b)# 虽然转为list 但是还是为[[1]]
# print b# [[1]]




