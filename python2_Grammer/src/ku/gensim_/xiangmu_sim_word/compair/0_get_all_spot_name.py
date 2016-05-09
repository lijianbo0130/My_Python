#coding=utf-8
'''
得到所有景区的名字 方便加入字典
'''
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import toolkit.data as dt

with open(r'data_comment2.txt','rb') as somefile:
    spot_name_set=set()
    lis_sen=[]# 存放分割完的句子
    for line in somefile:
        line= line.strip()
        spot_name=line.split("\t")[1]# 得到景点名字
        spot_name_set.add(spot_name)

            


with open(r'spot_name.txt','wb') as f:
    for spot_name_set in spot_name_set:
        line=spot_name_set+" 50"+" n"+"\n"
        f.write(line)
 
         
print "down"
        

