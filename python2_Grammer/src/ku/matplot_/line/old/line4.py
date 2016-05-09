#coding=utf-8
'''
多个子画板
'''

import matplotlib.pyplot as plt
import numpy as np

#等分0-5
x = np.linspace(0, 5, 11)
y = x ** 2
#2*3的要用数组转出来
fig, axes = plt.subplots(nrows=1, ncols=3)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

plt.show()