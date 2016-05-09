#coding=utf-8
'''
#深复制
a = [0, [1, 2], 3]
b = copy.deepcopy(a)
a[0] = 8
a[1][1] = 9
print a
print b
'''
import copy
a = [0, [1, 2], 3]
b = copy.deepcopy(a)# a的改变永远不会改变不b
