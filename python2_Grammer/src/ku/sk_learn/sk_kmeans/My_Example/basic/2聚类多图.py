#coding=utf-8
'''
Created on 2015年5月5日
@author: Administrator
'''
#coding=utf-8
'''
metrics用来计算
silhouette coefficient 值越大越好
'''
import numpy as np
from sklearn.cluster import KMeans
#metrics用来计算
from sklearn import metrics
import matplotlib.pyplot as plt
#===============================================================================
# 引包完成
#===============================================================================
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
#把x1 x2组合成一个矩阵
X = np.array(zip(x1, x2)).reshape(len(x1), 2)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Instances')
#在第一个页面画图  作为第一个分类
plt.scatter(x1, x2)
#其他类的 color 和markers
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
#test 为分成几个类
tests = [2,3,4,5,6,7,8]
subplot_counter = 1
for t in tests:
    subplot_counter += 1
    kmeans_model = KMeans(n_clusters=t).fit(X)
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
#     print metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')
    plt.title('K = %s, silhouette coefficient = %.03f' % (t, metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')))
#     plt.savefig(str(t)+"time.png")
#     plt.show()

