#coding=utf-8
'''
显示目录下的所有路径
'''
import os

#得到文件的路径
path=__file__
#分割 路径和文件名
fpath , fname = os.path.split(__file__)
#返回一个list
b=os.listdir(fpath)
print b
