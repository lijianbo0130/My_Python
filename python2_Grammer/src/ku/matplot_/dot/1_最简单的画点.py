#coding=utf-8
'''
Created on 2015年10月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


from pylab import *


x=[1,2,3]
y=[4,5,6]
#X和Y为相对应的numpy的矩阵
scatter(x,y,color='blue')
show()