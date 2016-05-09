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
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
#把x1 x2组合成一个矩阵
X = np.array(zip(x1, x2)).reshape(len(x1), 2)



K = range(2, 10)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans_model=kmeans.fit(X)
    print metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')
    print "1"
    meandistortions.append(metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean'))
plt.plot(K, meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Average distortion')
plt.title('Selecting k with the Elbow Method')
plt.show()

    
# plt.xlim([0, 10])
# plt.ylim([0, 10])
# plt.title('K = %s, silhouette coefficient = %.03f' % (t, metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')))
# plt.show()

