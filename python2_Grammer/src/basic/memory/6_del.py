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

from sys import getrefcount
if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c=a
    print(getrefcount(b)) # 3 a,b,c都指向
    
    del a# 删除a这个变量 但是b还是指向这个变量所以不会回收内存
#     print a # 报错
    print  b
    print(getrefcount(b)) # 只有c,b指向
    c=1
    print(getrefcount(b)) # 只有b指向