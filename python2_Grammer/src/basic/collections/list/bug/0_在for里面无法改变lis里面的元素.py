#coding=utf-8
'''
Created on 2015年8月21日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


'''
在for 循环中会锁死元素不管怎么样都无法改变lis中的元素
'''
# 对于常量
a=[1,2]
for num in a:
    print id(num)
    num =5
    print id(num)
    
print a

# 对于引用 也是同样
# a=[[1,2],[2,3]]
# for num in a:
#     print id(num)
#     num =1
#     print id(num)
# print a

