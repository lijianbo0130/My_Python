 #coding=utf-8
'''
Created on 2015年1月8日
@author: asus
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
z=x*x+y*y
ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
plt.show()
