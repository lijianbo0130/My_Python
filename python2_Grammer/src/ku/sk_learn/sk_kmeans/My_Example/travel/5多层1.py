#coding=utf-8
'''
首先挑出离群的点再聚类
'''
import tool
import matplotlib.pyplot as plt




class Spot():
    def __init__(self,name,jingdu,weidu,type_spot,score=0,flag=0):
        self.name = name
        self.jingdu = jingdu
        self.weidu = weidu
        self.type_spot = type_spot
        self.score = score
        self.flag=flag

        
   
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


def distance(spots_list): 
    spots_lis=spots_list   
    for spot in spots_lis:
        cur_spot=spot
        flag=0
        for spot in spots_lis:
            if cur_spot.name!=spot.name:
                dis=tool.data.jingweidu(cur_spot.jingdu, cur_spot.weidu, spot.jingdu, spot.weidu)
                if dis <5:
                    #附近有点<20
                    cur_spot.flag=1
                    continue
          
#辅助函数
spot=Spot(1,2,3,4)

spots_list=init_spots()
spots_lis=spots_list

jingdu_list=[]
weidu_list=[]
for spot in spots_lis:
    jingdu_list.append(spot.jingdu)
    weidu_list.append(spot.weidu)


distance(spots_lis)
for spot in spots_lis:
    print spot.flag
    
for i, spot in enumerate(spots_lis):
    if spot.flag==0:
        colo='b'
    else:
        colo='k'
    plt.plot(spot.jingdu, spot.weidu, color=colo, marker='D',ls='None')
plt.show()




