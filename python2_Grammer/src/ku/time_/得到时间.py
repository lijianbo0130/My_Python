# coding=utf-8
'''
Created on 2015年4月9日
@author: Administrator
'''
import time

#返回当前时间的时间戳
print "time.time(): %f " %  time.time()
print time.localtime( time.time() )
print time.asctime( time.localtime(time.time()) )

#ctime 得到当前时间
print time.ctime()
