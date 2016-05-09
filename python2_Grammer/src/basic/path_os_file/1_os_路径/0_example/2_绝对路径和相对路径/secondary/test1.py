#coding=utf-8
'''
Created on 2015年4月24日
@author: Administrator
'''

import sys
import os

def f():
    print sys.argv[0] # 引用本文件的的全路径加上引用文件啊的文件名 ---- 绝对路径\main.py
    print os.getcwd() # 引用本文件的文件夹全路径 ---绝对路径
    print os.path.dirname(__file__) #返回本文件文件夹路径  -----绝对路径和相对路径\secondary
    print os.path.abspath(__file__) #返回绝对全路径 -----绝对路径和相对路径\secondary\test1.py