#coding=utf-8
'''
Created on 2015年5月5日
@author: Administrator
'''

#coding=utf-8
'''
判断聚类的好坏
'''
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


#===============================================================================
# 数据初始化
#===============================================================================
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
#把x1 x2组合成一个矩阵   X为[[1 1] [2 3] [3 4]] 里面一个数据为一个向量
X = np.array(zip(x1, x2)).reshape(len(x1), 2)
print X
#===============================================================================
# 分为几个类
#===============================================================================
tests = 4
#===============================================================================
# kmean 调用   KMeans(n_clusters=tests)
#===============================================================================
kmeans_model = KMeans(n_clusters=tests).fit(X)
#===============================================================================
# 画图
#===============================================================================
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
# fix 完以后 kmeans_model.labels_ 里面的value代表分类标签
for index,value in enumerate(kmeans_model.labels_):
    plt.plot(x1[index], x2[index], color=colors[value], marker=markers[value],ls='None')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('K = %s' % (tests))
plt.show()
