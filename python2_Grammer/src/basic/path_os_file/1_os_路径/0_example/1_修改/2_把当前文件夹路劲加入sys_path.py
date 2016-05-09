#coding=utf-8
'''
Created on 2015年8月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os

#全路径 =__file__ 表示文件的全路径
path=__file__
#分割
fpath  = os.path.split(path)
sys.path.append(fpath)