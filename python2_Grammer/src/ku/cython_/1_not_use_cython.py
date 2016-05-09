#coding=utf-8
'''
Created on 2015年8月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import math
import toolkit.j_time as jt

def great_circle(lon1, lat1, lon2, lat2):
    '''
    是计算沿地球表面两点之间的距离的
    '''
    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) + 
                  (math.sin(a) * math.sin(b) * math.cos(theta)))

    return radius * c


@jt.timeit
def f(n):
    for i in range(n):
        great_circle(-72.345, 34.323, -61.823, 54.826)




f(500000) # f function use 2.95280158759 不优化使用的时间

