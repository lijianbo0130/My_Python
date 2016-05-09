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
import gc



gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)
a=[]
b=[]
a.append(b)
print 'a refcount:',sys.getrefcount(a)  # 2
print 'b refcount:',sys.getrefcount(b)  # 3

del a
del b
print gc.collect()  # 0