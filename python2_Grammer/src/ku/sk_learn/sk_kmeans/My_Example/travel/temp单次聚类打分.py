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
#metrics用来计算
from sklearn import metrics


#===============================================================================
# 数据初始化
#===============================================================================
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
#把x1 x2组合成一个矩阵
X = np.array(zip(x1, x2)).reshape(len(x1), 2)
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
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('K = %s, silhouette coefficient = %.03f' % (tests, metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')))
plt.show()
