#coding=utf-8
'''
Created on 2015年5月6日
@author: Administrator
'''

#在当前目录下创建a文件
import os
print os.getcwd()
#如果存在
if os.path.exists("b"):
    print "True"
    print os.getcwd()
#不存在
else:
    #得到当前路径
    path=os.getcwd()
    path=os.path.join(path,"b")
    #创建文件夹
    os.mkdir(path)
    #改变当前路径
    os.chdir(path)
    print os.getcwd()
