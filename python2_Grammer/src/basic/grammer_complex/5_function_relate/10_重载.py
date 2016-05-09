#coding=utf-8
'''
Created on 2015年11月9日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

# PYTHON没有重载只能在一个函数里面把不需要赋值的变量在参数里面赋值
def f(a,b=None):
    print b
    
    
if __name__ == '__main__':
    lis=[1,2,3]
    f(lis) 