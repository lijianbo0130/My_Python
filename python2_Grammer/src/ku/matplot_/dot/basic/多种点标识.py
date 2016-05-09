#coding=utf-8
'''
Created on 2015年5月5日
@author: Administrator
'''
from pylab import *
colors = ['b', 'g', 'c', 'm', 'y', 'k']
markers = ['o', 's', 'D', 'v', '^', '*','d','<','>','1','2']



for i in range(len(colors)):
    for j in range(len(markers)):
        plt.plot(i, j, color=colors[i], marker=markers[j])

plt.xlim(-1, len(colors)+1)
plt.ylim(-1, len(markers)+1)        
plt.show()