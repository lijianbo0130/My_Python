#coding=utf-8
'''
Created on 2015年5月5日
@author: Administrator
'''
def KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, 
           tol=0.0001, precompute_distances='auto', verbose=0, 
           random_state=None, copy_x=True, n_jobs=1):
    '''
    kmeans算法初始化
    :param n_clusters: 聚集成几个类
    int, optional, default: 8
The number of clusters to form as well as the number of centroids to generate.
    :param init:
    :param n_init:
    :param max_iter:
    :param tol:
    :param precompute_distances:
    :param verbose:
    :param random_state:
    :param copy_x:
    :param n_jobs:
    '''
    