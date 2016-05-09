# coding=utf-8
'''
绘制景点的经纬度图片
'''

import tool
import matplotlib.pyplot as plt 
import numpy as np



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

#经度坐标 纬度坐标
jingdu_list=[]
weidu_list=[]
for spot in spots_lis:
    jingdu_list.append(spot.jingdu)
    weidu_list.append(spot.weidu)
jingdu_list=np.array(jingdu_list)
weidu_list=np.array(weidu_list)



#画图
plot1 = plt.plot(jingdu_list, weidu_list, 'go')
#改变x轴和y轴的大小
plt.xlim(jingdu_list.min(), jingdu_list.max())
plt.ylim(weidu_list.min(), weidu_list.max())
# #添加标签
plt.legend([plot1], ('redlinae'), 'best', numpoints=1)


plt.show()
    

    
# # 初始化游玩参数
# travel = Travel(8, 12, 13.5, 17.5, 19, 22)
# # 初始化用户信息  经度纬度 游玩天数  当前时间
# user = User(117.947214, 24.564469, 2, 8.0, One_hour_speed=10, Bus_time=1.5)
# # 初始化景点信息
# list_spots = init_spots()
# # 用来记录旅游
# travel_list = []
# #
# onece_one_spot(user, travel, list_spots, travel_list)
# print "down"


