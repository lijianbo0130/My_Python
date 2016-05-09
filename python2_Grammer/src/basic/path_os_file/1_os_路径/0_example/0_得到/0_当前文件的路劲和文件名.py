#coding=utf-8
'''
Created on 2015年4月17日
@author: Administrator
'''
import os




#得到当前的文件名全信息  两个都可行
# print sys.argv[0]
# print __file__



#全路径 =__file__ 表示文件的全路径
path=__file__
#分割
fpath , fname = os.path.split(path)
print fpath 
# 防止中文编码不能打印出来
print fname.decode('gbk','ignore')

