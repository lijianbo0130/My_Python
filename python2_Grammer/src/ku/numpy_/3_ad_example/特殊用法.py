#coding=utf-8
'''
Created on 2015年2月8日
@author: asus
'''

import numpy as np
#得到一列
# a=np.mat([[1,2,3],[4,5,6],[7,8,9]])
# b=a[:,1]
# print(b)



#按数组某一行的第一个数来分割数组
# a=np.mat([[1,2,3],[4,5,6],[7,8,9]])
# mat0 = a[np.nonzero(a[:,0] > 4)[0],:][0]
# print(mat0)
# c=a[:,1]>0
# print(c)
# b=np.nonzero(a[:,1]>0)
# print(b)
# d=np.nonzero(a[:,1]>0)[0]
# print(d)



#数组的最后一列的数值是否全部相等
# a=np.mat([[1,2,9],[4,5,9],[7,8,9]])
# b=len(set(a[:,-1].T.tolist()[0])) == 1
# print(b)

#数组里面的值不用取出来也可以比较
# m=[1,2,3]
# m=np.mat(m)
# print m
# print m[0:1,0]
# if m[0:1,0]==1:
#     print True
# else:
#     print False

#得到数组里面某个值
# m=[1,2,3]
# m=np.mat(m)
# print m
# #取1
# print m[0,0]


# a=np.mat([[1,2,3],[4,5,6],[7,8,9]])
# #取5
# print a[1,1]
# #取出5矩阵
# print a[1:2,1:2]

#数字乘矩阵
# m=[1,2,3]
# m=np.mat(m)
# m=2*m
# print m

#得到数组里面某个值
# a=[1,2,3]
# a=np.mat(a)
# for i in range(3):
#     print a[0,i]





