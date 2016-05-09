#coding=utf-8
'''
Created on 2015年5月13日
@author: Administrator
'''
import os
import time

#得到文件最后修改时间
t=os.path.getmtime("join_v.py")
print t # 1430879037.68   以浮点形式返回自Linux新世纪以来经过的秒数
#
tt =time.ctime(t)
print tt
