#coding=utf-8
'''
多个子画板
'''

import matplotlib.pyplot as plt
import numpy as np

#等分0-5
x = np.linspace(0, 5, 11)
y = x ** 2

fig, ax = plt.subplots(figsize=(6,6))

#lw linewidth 线的宽度
ax.plot(x, x+1, color="blue", lw=25)


#ls  linestyle  线的样式
# # possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
# ax.plot(x, x+5, color="red", lw=2, ls='*')
# ax.plot(x, x+5, color="red", lw=2, ls='-')
# ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')


# # custom dash
# line, = ax.plot(x, x+8, color="black", lw=1.50)
# line.set_dashes([5, 10]) # format: line length, space length, ...

#线上加标记
# # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
# ax.plot(x, x+ 9, color="green", lw=2, ls='-', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='*', marker='o')
# ax.plot(x, x+11, color="green", lw=2, ls='*', marker='s')
# ax.plot(x, x+12, color="green", lw=2, ls='*', marker='1')

# # marker size and color
# ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
# ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
# ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");

plt.show()