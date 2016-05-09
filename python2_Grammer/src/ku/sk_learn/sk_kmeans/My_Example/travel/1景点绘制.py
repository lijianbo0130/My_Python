# coding=utf-8
'''
单纯的一个景点一个景点的玩
第二版
'''

import tool





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
#画图
tool.data.draw_dot(jingdu_list, weidu_list, 0.05)


    

    



