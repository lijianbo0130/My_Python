#coding=utf-8
'''
Created on 2015年6月1日
@author: Administrator
'''
import numpy as np

a=[[1,2],[4,5]]
a=np.mat(a)

print a.sum()# 12 全部数据加起来
print a.sum(axis=0) # [[5 7]] 按照列加起来
print a.sum(axis=1) # [[3] [9] ] 按照行加起来