#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：
讲解对象的引用
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


class From_obj():
    def __init__(self):
        pass

if __name__ == '__main__':
    '''
    对象的引用地址也是一样的
    '''
    c=From_obj()
    b=c
    print(id(c))
    print(id(b))
