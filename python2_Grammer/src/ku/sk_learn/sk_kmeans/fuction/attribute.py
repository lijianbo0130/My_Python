#coding=utf-8
'''
kmeans_model.cluster_centers_   
集群中心的坐标   
[[ 8.66666667  2.        ]
 [ 1.75        2.        ]
 [ 5.4         6.8       ]
 [ 7.          1.        ]]
n_clusters 行   n_features 列

kmeans_model.labels_ : 
Labels of each point  每一类所属的标签 从0开始 [1 1 1 1 2 2 2 2 2 3 0 0 3 0]

inertia_ : float
Sum of distances of samples to their closest cluster center.
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
#把x1 x2组合成一个矩阵
X = np.array(zip(x1, x2)).reshape(len(x1), 2)
#===============================================================================
# 分为几个类
#===============================================================================
tests = 4
#===============================================================================
# kmean 调用   KMeans(n_clusters=tests)
#===============================================================================
kmeans_model = KMeans(n_clusters=tests).fit_transform(X)
print kmeans_model
kmeans_model1 = KMeans(n_clusters=tests).fit(X)
print type(kmeans_model1.cluster_centers_)
#===============================================================================
# 画图
#===============================================================================
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
# markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
# for i, l in enumerate(kmeans_model.labels_):
#     plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
# for c1,c2 in kmeans_model.cluster_centers_:
#     plt.plot(c1, c2, color='k', marker='D',ls='None')
# plt.xlim([0, 10])
# plt.ylim([0, 10])
# plt.title('K = %s' % (tests))
# plt.show()


