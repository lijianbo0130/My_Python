#coding=utf-8
'''
这里介绍array的常用操作
'''
from __future__ import  division
import numpy as np
 
 
 
  
   
     
#乘法 A*B  逐个元素相乘  
# a= np.array([1,2])  
# b= np.array([3,4])  
# c=a*b
# print(c) #[3 8] [1*3,2*4]
         
#矩阵乘法
# a= np.array([1,2])  
# b= np.array([3,4])  
# c=np.dot(a,b) 
# print(c) #1*3+2*4  1*2 2*1
 
#bool运算
# a=np.array([[1,2],[2,3],[4,5]])
# bool_index=(a>2)# 得到大于2的下标
# print bool_index # [[False False] [False  True] [ True  True]]  得到大于2的下标为矩阵
# print a[bool_index]# 变成一位数组后的下标 [3 4 5]
# print a[a>2]# [3 4 5]
 
 
# 加法
a= np.array([1,2])  
b= np.array([3,4])  
# print a+b # [4 6] 对应的元素相加 [1+3,2+4]
# print np.add(a,b)# [4 6] add和+相同
 

 
# 除法
# a= np.array([1,2])  
# b= np.array([3,4])  
# print a / b# from __future__ import  division 这样不会出现1/2=0
 
# 开方
# print np.sqrt(a)#  [ 1.          1.41421356] 每个元素开方
 
# 次方
# a= np.array([1,2])  
# print a**2
 
 
 
 
# sum
# x = np.array([[1,2],[3,4]])
# print np.sum(x)  # Compute sum of all elements; prints "10"
# print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
# print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"
 
# 转置
# x = np.array([[1,2], [3,4]])
# print x    # Prints "[[1 2] [3 4]]"
# print x.T  # Prints "[[1 3] [2 4]]"
# # Note that taking the transpose of a rank 1 array does nothing:
# v = np.array([1,2,3])
# print v    # Prints "[1 2 3]"
# print v.T  # Prints "[1 2 3]"
 
# min(0) max(0)  0表示列的最小   1表示行的最小
# a=np.array([[1,2,3],[4,5,2]])
# b=a.min(1)
# print(b)
# b=a.min(0)
# print b
# print(b[0,0])
 
 
 
 
 
 
 
#赋值
# a=np.array([[1,2,3],[4,5,2]])
# b=a[0,:]
# print(b)
# b=a[0:1,:]
# print(b)
# b=a[0:2,:]
# print(b)
# b=a[0,1:2]
 


