#coding=utf-8
'''
不使用for循环使用矩阵相乘能提高速度
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from numpy import random
import toolkit.j_time as ti

@ti.timeit
def  for_loop():
#     print [w.dot(lis_vec[i]) for i in range(n)]
    [w.dot(lis_vec[i]) for i in range(n)]
    
@ti.timeit
def not_for_loop():
#     print w.dot(maxtrix_vex)
    w.dot(maxtrix_vex)
    

n=500
d=3000
c=500
w=random.rand(c,d)
lis_vec=[random.rand(d,1) for i in range(n)]
maxtrix_vex=random.rand(d,n)


'''
不使用for循环差不多快一倍
c*d的矩阵乘以d*n
'''
for_loop() # 1.22462712199
not_for_loop() # 0.560458414156
 


