#coding=utf-8
'''
多个子画板画曲线
'''

import matplotlib.pyplot as plt
import numpy as np

#等分0-5
x = np.linspace(0, 5, 11)
y = x ** 2
#创建画板
fig = plt.figure()
#占大图的比例
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title');
# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');
plt.show()
