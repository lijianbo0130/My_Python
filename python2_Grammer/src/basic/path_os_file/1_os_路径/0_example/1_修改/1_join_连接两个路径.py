#coding=utf-8
'''
连接两个路径
#a\b
# print os.path.join("a","b")
'''
import os
path=__file__
fpath  = os.path.split(path)[0]
print fpath 
print os.path.join(fpath,"lijianbo")