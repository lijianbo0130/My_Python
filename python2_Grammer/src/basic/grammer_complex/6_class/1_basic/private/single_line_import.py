#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

from single_line_double_line import _my_single# _my_single 可以访问
# from single_line_double_line import * # 无法访问
_my_single()