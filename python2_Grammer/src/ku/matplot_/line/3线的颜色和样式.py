#coding=utf-8
'''
调整线的颜色和样式
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
# 画出图像 设置线的颜色和宽度
plt.plot(x,y,color="blue",linewidth=3.0)
# 显示图像
plt.show()
