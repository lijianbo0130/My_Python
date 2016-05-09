#coding=utf-8
'''
绘制一个简单的函数然后添加标题
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


import matplotlib.pylab as plt
import numpy as np


# 画图需要有x的数据和对应的y的数据
# X 是一个 numpy 数组，包含了从-pi到pi等间隔的 256 个值。
x=np.linspace(-np.pi, np.pi, 256, True)
# y为这 256 个x值对应的y值
y=np.sin(x)
# 画出图像
plt.plot(x,y)
# 添加标题
plt.xlabel('x value')
plt.ylabel('sin(x)')
# 显示图像
plt.show()
