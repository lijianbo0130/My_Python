#coding=utf-8
'''
设置x和y的取值
plt.xlim(X.min()*0.95, X.max()*1.05) #x
plt.ylim(C.min()*0.95, C.max()*1.05) #y

# 设置横轴记号  X上显示 -4 -3 -2 -1 0 1 2 3 4  9个数字 默认为ture
# plt.xticks(np.linspace(-4,4,9,endpoint=True)) #X
# plt.yticks(np.linspace(-1,1,5,endpoint=True)) #y
'''

import matplotlib.pyplot as plt 
import numpy as np




# '''X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。
# C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。'''
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C = np.cos(X)
# 绘制余弦曲线，
plt.plot(X, C)

# 设置横轴的上下限
plt.xlim(-4.0,4.0)
# 设置横轴记号  X上显示 -4 -3 -2 -1 0 1 2 3 4  9个数字 默认为ture
# plt.xticks(np.linspace(-4,4,9,endpoint=True))

plt.show()

