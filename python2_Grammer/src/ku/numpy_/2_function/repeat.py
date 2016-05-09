#coding=utf-8
'''
Created on 2015年7月24日
@author: Administrator
'''
import numpy as np
# 把一个向量
a=np.mat([1,2,3])
b=np.repeat(a,2,axis=0) # 列赋值
print b

# 把一个向量
a=np.mat([1,2,3])
b=np.repeat(a,2,axis=1) # 行复制
print b


