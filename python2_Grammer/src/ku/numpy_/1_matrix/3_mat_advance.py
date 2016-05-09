#coding=utf-8
'''
Numpy matrices必须是2维的
'''

import numpy as np



#转置矩阵

# T
# a=np.mat([1,2,3]) 
# print a # [[1 2 3]]
# print a.T # [[1] [2] [3]]

# transpose  和T一样
# print a.transpose() # [[1] [2] [3]]

# 减法
# a=np.mat([[0],[0]])
# b=np.mat([[1],[1]])
# print a-b # [[-1] [-1]]

# 加法
# a=np.mat([[0],[0]])
# b=np.mat([[1],[1]])
# print a+b # [[1] [1]]



#矩阵相乘  dot和 *乘是一样的
# a=np.mat([1,2,3])
# print a*a.T # [[14]]
# print np.dot(a,a.T)# 1行3列*3行1列  1*1+2*2+3*3


#inner 前面一个乘以后面一个的转置
# b=[1,2,3]
# b=np.mat(b)
# 
# d=np.inner(b,b)# b*bT
# e=b*b.T
# print e # [[14]]
# print d # [[14]]
# 
# d=np.inner(b.T,b.T)# b.T*b
# e=b.T*b
# print e # [[14]]
# print d # [[14]]



#矩阵对应元素相乘  对应位置元素相乘
# a=np.mat([1,2,3])
# d=np.multiply(a,a)
# print(d)# [[1 4 9]]











#解方程
# a=[[1,2,1],[2,-1,3],[3,1,2]]
# a=np.array(a)
# b=[7,7,18]
# x=np.linalg.solve(a,b)
# print(x)
# c=np.dot(a,x)
# print(c)




#求矩阵x的特征值和特征向量，特征值保存在a中，特征向量保存在b中
# a,b=np.linalg.eig(a)
# print(a)
# print(b)

#协方差矩阵
# s=[100,120,140]
# t=[50,60,70]
# y=s+t
# y=[s,t]
# a=np.cov(y)
# print(a)

#矩阵转list
#1*3
# a=[1,2,3]
# a=np.mat(a)
# b=a.tolist()[0]
# print(b)
#3*3
# b=a.tolist()
# print(b)
# print(b[1])
# a=[[2],[1],[0]]
# a=np.mat(a)
# b=a.tolist()
# print(b)
# b=a.T.tolist()
# print(b[0])

# np.linalg.det(a)   #返回的是矩阵a的行列式
# np.linalg.norm(a,ord=None)  
#  #计算矩阵a的范数
# np.linalg.eig(a)  
#  #矩阵a的特征值和特征向量
# np.linalg.cond(a,p=None)  
#  #矩阵a的条件数
# np.linalg.inv(a)  





 


