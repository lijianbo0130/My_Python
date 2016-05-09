#coding=utf-8
'''
Created on 2015年4月30日
@author: Administrator
'''

import tool

class Spot():
    def __init__(self,name,jingwu,weidu,type_spot,score=0):
        self.name = name
        self.jingwu = jingwu
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
#         # 时间转成数字  6：30 =6.5
#         start = tool.data.time_to_float(line[3])
#         end = tool.data.time_to_float(line[4])
#         rec_time = float(line[5].split("H")[0])
#         spot = Spot(name, jd, wd, start, end, rec_time)
        spots_list.append(spot)
    return spots_list



                
#辅助函数
spot=Spot(1,2,3,4)


spots_list=init_spots()
#如果直接使用 spots_list会出bug 转成令一个变量就不会发生bug
spots_lis=spots_list
for spot in spots_lis:
    print spot.type_spot
