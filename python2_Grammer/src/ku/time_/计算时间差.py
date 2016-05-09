#coding=utf-8
'''
两种方式
'''
import datetime    
starttime = datetime.datetime.now()   
for i in range(10000):
    pass
#long running    
endtime = datetime.datetime.now()    
print (endtime - starttime).seconds,"sec"#以秒计算 2
print (endtime - starttime)  #全部时间  0:00:00.208000


import time    
starttime = time.clock()   
for i in range(10000):
    pass
#long running    
endtime = time.clock() 
# print (endtime - starttime).seconds #以秒计算 2
print (endtime - starttime)  #全部时间  0:00:00.208000