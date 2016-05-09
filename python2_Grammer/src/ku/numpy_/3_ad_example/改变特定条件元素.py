'''
Created on 2015年2月5日
@author: asus
'''
import numpy as np
dataMatrix=np.array([[1,2],[3,4]])
print(dataMatrix)
# #列
# a=dataMatrix[:,0]
# print(a)
# #行
# a=dataMatrix[0,:]
# print(a)
print(dataMatrix[:,0] <= 1)


retArray=np.array([[1,2],[3,4]])
# 把对应的一列都变成-1
retArray[dataMatrix[:,0] <= 10] = -1.0
print(retArray)
