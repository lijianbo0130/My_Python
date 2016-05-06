#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

import jieba


import datetime    
starttime = datetime.datetime.now()   
 



#readline  全部读出来=====================================================
f1=open(r'C:\Users\asus\Desktop\data\travel\super.txt','r')
count=0
while True:
    #读取一行
    w=f1.readline()
    #精确模式
    seg_list = jieba.cut(w, cut_all=False)
    #全模式
#     seg_list = jieba.cut(w, cut_all=True)
    if not w :
        break 
    count=count+1
    print count

endtime = datetime.datetime.now()    
print (endtime - starttime).seconds #以秒计算
# print (endtime - starttime)   #全部时间
# 全模式26秒
# 精确模式21秒

