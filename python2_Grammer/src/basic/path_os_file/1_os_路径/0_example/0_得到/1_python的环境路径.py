#coding=utf-8
'''
Created on 2015年8月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
python 执行import的时候会去 sys.path的路径里面找文件
在eclipse中会自动把当前文件的目录加到sys.path中
'''
print sys.path