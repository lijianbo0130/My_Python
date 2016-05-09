'''
Created on 2015年1月8日

@author: asus
'''





from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

#画面
fig = plt.figure()
ax = fig.gca(projection='3d')
#从-5 到5 每一步0.25
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
#网格 meshgrid用于从数组a和b产生网格
x, y = np.meshgrid(x, y)
z=x*x+y*y
#rstride
#cstride 表示颜色变化的快慢
#antialiased 抗锯齿
#linewidth 网格线的宽度
#cmap颜色类型
surf = ax.plot_surface(x, y, z, rstride=2, cstride=2,cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()

