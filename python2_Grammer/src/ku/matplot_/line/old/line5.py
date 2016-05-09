#coding=utf-8
'''
多个子画板
'''

import matplotlib.pyplot as plt
import numpy as np

#等分0-5
x = np.linspace(0, 5, 11)
y = x ** 2
#长和宽
fig, axes = plt.subplots(figsize=(12,3))
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
plt.show()