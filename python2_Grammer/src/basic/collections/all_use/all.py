#coding=utf-8
'''
有0或者"" 为flase 
[]() 为true
说明：如果iterable的所有元素不为0,'',或者iterable为空，
all(iterable)返回，否则返回
'''
from __future__ import  division

print all(['a', 'b', ' ', 'd'])  # True
print all(['a', 'b', '', 'd'])  #  ""为false
print all([0,2,3])  # 0为false
print all([]) # True


