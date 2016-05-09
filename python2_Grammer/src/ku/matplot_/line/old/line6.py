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
fig, ax = plt.subplots()
ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=3); # 设置标题的位置
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title');
plt.show()