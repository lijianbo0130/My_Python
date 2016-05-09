#coding=utf-8
'''
sys.argv[]是用来获取命令行参数的，
sys.argv[0]表示代码本身文件路径,因此要从第二个即sys.argv[1]开始取参数。
'''
import os
import sys



#得到这个文件的路径和引用文件无关
# print os.path.dirname(__file__) #返回本文件文件夹全路径 
# print os.path.abspath(__file__) #返回绝对全路径包括本文件的文件名

#都是引用本文件的文件夹在哪  输出的目录就在哪
# print sys.argv[0] #引用文件的全路径加上引用文件啊的文件名
# print os.getcwd() #引用文件的文件夹全路径





#tempfile.gettempdir 用于返回保存临时文件的文件夹路径。
# import tempfile
# print tempfile.gettempdir()







