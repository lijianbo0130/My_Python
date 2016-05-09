#coding=utf-8
'''
Created on 2015年6月1日
@author: Administrator
'''
import numpy as np
#把a 正规化为长度为1的向量
a=[1,1]
a=np.array(a)
a=np.divide(a,np.sqrt(np.sum(np.power(a,2))))
print a
# a=[4,5,2,6,9,8,7,2,6]


# x=math.power(x,1.0/3)
