#coding=utf-8
'''
用coefficient 来测试
'''
import tool
import matplotlib.pyplot as plt




class Spot():
    def __init__(self,name,jingdu,weidu,type_spot,score=0,c_flag=0):
        self.name = name
        self.jingdu = jingdu
        self.weidu = weidu
        self.type_spot = type_spot
        self.score = score
        self.c_flag=c_flag

        
   
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

def get_sort_coefficient(list_coefficient):
    sort_coefficient=sorted(list_coefficient, key=lambda list_coefficient : list_coefficient[1],reverse=True)   # sort by age   
    return sort_coefficient

          
#辅助函数
spot=Spot(1,2,3,4)

spots_list=init_spots()
spots_lis=spots_list

jingdu_list=[]
weidu_list=[]
for spot in spots_lis:
    jingdu_list.append(spot.jingdu)
    weidu_list.append(spot.weidu)


list_coefficient=tool.ml.km.get_coefficient(jingdu_list, weidu_list, 20)
sort_coefficient=get_sort_coefficient(list_coefficient)
cur_coe=sort_coefficient[1]
cur_coe_lable=cur_coe[2].labels_.tolist()

# 把分类的标签加上
for index,value in enumerate(cur_coe_lable): 
    spots_lis[index].c_flag=value

#输出标签
for spot in spots_lis:
    print spot.name,spot.c_flag
    
#生成一个list 记录个个分类的指标











