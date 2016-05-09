#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：
id 得到变量的内存地址
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


if __name__ == '__main__':
    '''
    id 得到变量的内存地址
    '''
    a = 1
    b = 1
    print(id(a))
    print(id(b))