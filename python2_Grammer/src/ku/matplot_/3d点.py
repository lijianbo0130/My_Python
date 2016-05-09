#coding=utf-8
'''
用法：linspace(x1,x2,N)
功能：linspace是Matlab中的均分计算指令，用于产生x1,x2之间的N点行线性的矢量。其中x1、x2、N分别为起始值、终止值、元素个数。若默认N，默认点数为100。

'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mimport numpy as npmport plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)
# ax.clabel(cset, fontsize=9, inline=1)
# x=np.linspace(0, 1, 100)
# y=np.linspace(0, 1, 100)
# x = np.arange(-5, 5, 0.25)
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)
# z=x*x+y*y
# surf = ax.plot_surface(x, y, z, rstride=2, cstride=2,cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)
#ax.plot(x, y, z)
ax.scatter(0, 0, 0,c='r',marker='o')
#plot(1,1,1,zdir='z')
plt.show()
