#coding=utf-8
'''
Created on 2015年6月1日
@author: Administrator
'''
import numpy as np
# devide和/符号效果一样
a=[1,2,3,4,5]
a=np.array(a)
print np.divide(a,float(5)) # 要加float 不然会成为0 0 0 0 1
print a/5.0