#coding=utf-8
'''
fit(X[, y])    Compute k-means clustering
__init__(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)[source]

fit(X, y=None)
Compute k-means clustering.
Parameters:    X : array-like or sparse matrix, shape=(n_samples, n_features)
初始化后调用计算聚类
kmeans_model = KMeans(n_clusters=tests).fit(X)
'''