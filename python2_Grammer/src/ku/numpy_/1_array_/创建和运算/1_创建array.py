#coding=utf-8
'''
array常用matrix基本不用
numpy arrays (ndarrays) 
可以是多维的（1D，2D，3D····ND）. 
Matrix是Array的一个小的分支，
包含于Array。所以matrix 拥有array的所有特性。
'''
import numpy as np
# #一纬数组
# a=np.array([1,1])
# print a[0] # 第一个元素1
# print a[0:]# [1 1] 第一纬的所有

#二维数组  和数组用法一样
a=np.array([[1,1],[2,2],[2,2]])# 3行2列
print a

# # 逗号  前面表示行,后面表示列 
# 输出某一行
print a[0] 
print a[0,]
print a[0,:]
# print a[0,0] # 1 表示第0行第0个元素

# # :表示从a到b不包括b 如果后面没有字符表示一直到结尾
# print a[0:] # [[1 1] [2 2] [2 2]] 表示从第一行到最后一行
# print a[0:1]# [[1 1]]  行从0到1 只包含0
# print a[0:1,0:1]# [[1]]  行从0到1 列从0到1  只包含0


# 把 1*12的向量转为矩阵
# a=[1,2,3,4]
# a=np.array(a)
# print a
# a=a.reshape(4,1) # 4*1的矩阵
# print a

# 修改元素
# a=np.array([1,2,3])
# a[0]=50# 修改数字元素
# print a # [50  2  3]

# # 修改和查看array里面数据的数据类型
# a=np.array([1,2,3])
# print a.dtype
# # 变成float 类型
# a=np.array([1,2,3],dtype=np.float16)
# # int 类型 np.fromstring(s, dtype=np.int16)
# print a

# # array 数据类型
# print type(a) #numpy.ndarray
