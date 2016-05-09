#coding=utf-8
'''
最终版本
'''
from sklearn import metrics
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import numpy as np
import tool


#metrics用来计算  silhouette_coefficient
class Spot():
    def __init__(self,name,jingdu,weidu,type_spot,score=0,clus_flag=0,clus_jingdu=0,clus_weidu=0):  
        '''
        景点对象
        :param name: 景点名称
        :param jingdu:经度
        :param weidu:纬度
        :param type_spot:景点类型
        :param score:景点得分
        :param clus_flag:景点所属类别
        :param clus_jingdu 中心点经度
        :param clus_weidu 中心点纬度
        '''
        self.name = name
        self.jingdu = jingdu
        self.weidu = weidu
        self.type_spot = type_spot
        self.score = score
        self.clus_flag=clus_flag
        self.clus_jingdu=clus_jingdu
        self.clus_weidu=clus_weidu

class spot_cluster():
    def __init__(self,spot_list,jingdu,weidu,score=0):
        self.spot_list = spot_list
        self.jingdu = jingdu
        self.weidu = weidu
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

# 传入一个spot_list返回 x_list y_list
def get_x_y_list(spots_list):
    x=[];y=[]
    spots_lis=spots_list
    for spot in spots_lis:
        x.append(spot.jingdu);y.append(spot.weidu)
    return x,y

#返回一个list 变量为  k分为几类,km对象,得分
def get_cluster(x,y,max_cluster):
    '''
    传入x和y的list  返回coefficient指数的一个list [k,coefficient系数,kmeans_model]
    silhouette_coefficient 的值越大越好
    :param x: x list
    :param y: y list '''
    #定义list 变量为  k分为几类,km对象,得分
    list_coefficient=[]
    #转成array
    x=np.array(x)
    y=np.array(y)
    X = np.array(zip(x, y)).reshape(len(x), 2)
    K = range(2, max_cluster)
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans_model=kmeans.fit(X)
        list_coefficient.append([k,
                                 kmeans_model,metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')])    #得到coe最大值的下标 并返回
    list_index =[k3 for k1,k2,k3 in list_coefficient].index(max([k3 for k1,k2,k3 in list_coefficient]))
    return list_coefficient[list_index]
    
#传入一没有分类的list 返回分类后的多个list 改变c_flag值
def sigle_km(spots_list):
    spots_lis=spots_list
    #转成list
    x,y=get_x_y_list(spots_list)    
    #得到分类组的编号
    list_coefficient=get_cluster(x,y,len(spots_list)/2+1)
    #合并 返回 得到分类的list
    cluster_list=list_coefficient[1].labels_.tolist()
    center_list=list_coefficient[1].cluster_centers_
    #标签添加完成
    for index,spot in enumerate(spots_lis):
        spot.c_flag=cluster_list[index]
        spot.clus_jingdu=center_list[cluster_list[index]][0]
        spot.clus_weidu=center_list[cluster_list[index]][1]
    #聚成多个类别[[cluster1],[cluster2],...]
    mult_list=[]
    for i in range(max(cluster_list)+1):
        cur_list=[]
        for index,spot in enumerate(spots_lis): 
            if spot.c_flag==i:
                cur_list.append(spot)
        mult_list.append(cur_list)
    return mult_list


#传入spots_list 为没有聚类的spot_list 和中心点的经纬度
def recur_km(spots_list): 
    global max_cluster
    print len(spots_list)
    #终止条件
    if len(spots_list)<=max_number_of_a_cluster:
        spots_lis=spots_list
        #一个cluslist
        cur_clus=[]
        for spot in spots_lis:
            spot.c_flag=max_cluster#BUG
            cur_clus.append(spot)
        #把cur_clus变成对象   
        max_cluster+=1
    
        return
    mult_spots_list=sigle_km(spots_list)
    for spots in mult_spots_list:
        recur_km(spots)
        
    
    
          
#辅助函数
spot=Spot(1,2,3,4)
max_cluster=0
max_number_of_a_cluster=5

#===============================================================================
# 景点信息初始化
#===============================================================================
spots_list=init_spots()
spots_lis=spots_list
#===============================================================================
# 景点聚类初始化  
#==============================================================================
spot_cluster_list=[]
recur_km(spots_lis)
for spot in spots_lis:
    print spot.name,spot.clus_jingdu,spot.clus_weidu,spot.clus_flag


#===============================================================================
# 画图
#===============================================================================
# colors = ['b', 'g', 'c', 'm', 'y', 'k']
# markers = ['o', 's', 'D', 'v', '^', '*','d','<','>','1','2']
# for i, spot in enumerate(spots_lis):
#     plt.plot(spot.jingdu, spot.weidu, color=colors[spot.c_flag/len(markers)], marker=markers[spot.c_flag%len(markers)],ls='None')
# plt.title('max_clu = %s, max_num = %s' % (max_cluster,max_number_of_a_cluster))
# plt.savefig(str(max_number_of_a_cluster)+".png",dpi=1000)
# plt.show()









