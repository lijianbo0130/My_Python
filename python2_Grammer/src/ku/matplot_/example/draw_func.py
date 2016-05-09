#coding=utf-8
'''
Created on 2015年12月17日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import numpy as np
import matplotlib.pylab as plt

def jieceng(x):
    r=1
    while x>0:
        r=r*x
        x-=1
    return r

print jieceng(4)
# 画图需要有x的数据和对应的y的数据
# X 是一个 numpy 数组，包含了从-pi到pi等间隔的 256 个值。
x=np.linspace(0, 1, 256, True)
# y为这 256 个x值对应的y值
c=jieceng(10)/(jieceng(6)*jieceng(3))
y=c*pow(x,6)*pow(1-x,3)
# 画出图像
plt.plot(x,y)
plt.grid(True)
# 显示图像
plt.show()