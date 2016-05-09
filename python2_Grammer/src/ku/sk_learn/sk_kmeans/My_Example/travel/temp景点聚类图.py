#coding=utf-8
'''
Created on 2015年5月5日
@author: Administrator
'''

import tool
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.cluster import KMeans
#metrics用来计算
from sklearn import metrics



class Spot():
    def __init__(self,name,jingdu,weidu,type_spot,score=0):
        self.name = name
        self.jingdu = jingdu
        self.weidu = weidu
        self.type_spot = type_spot
        self.score = score

        
   
# 初始化景区信息
def init_spots():
    spots_list = []
    f1 = tool.file_t.read_line(r"q3.txt")
    for line in f1:
        line = line.split("\t")
        name = line[0]
        type_spot=line[1]
        # 经纬度转float
        jd = float(line[2])
        wd = float(line[3])
        spot=Spot(name,jd,wd,type_spot)
        spots_list.append(spot)
    return spots_list


                
#辅助函数
spot=Spot(1,2,3,4)


spots_list=init_spots()
spots_lis=spots_list

jingdu_list=[]
weidu_list=[]
for spot in spots_lis:
    jingdu_list.append(spot.jingdu)
    weidu_list.append(spot.weidu)
    
jingdu_list=np.array(jingdu_list)
weidu_list=np.array(weidu_list)
X = np.array(zip(jingdu_list, weidu_list)).reshape(len(jingdu_list), 2)

#===============================================================================
# 分为几个类
#===============================================================================
tests = 9
#===============================================================================
# kmean 调用   KMeans(n_clusters=tests)
#===============================================================================
kmeans_model = KMeans(n_clusters=tests).fit(X)
#===============================================================================
# 画图
#===============================================================================
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'blue','black']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', 'D','D']
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(jingdu_list[i], weidu_list[i], color=colors[l], marker=markers[l],ls='None')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('K = %s, silhouette coefficient = %.03f' % (tests, metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')))



plt.xlim(jingdu_list.min()*0.9999, jingdu_list.max()*1.0001)
plt.ylim(weidu_list.min()*0.9999, weidu_list.max()*1.0001)
plt.show()
    