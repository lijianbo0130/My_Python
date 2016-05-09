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
    '''
    在容器中也会增加引用
    '''
    a = [1, 2, 3]
    print(getrefcount(a)) #2
    b = [a, a]
    print(getrefcount(a))# 因为b容器中引用了两次所以为4