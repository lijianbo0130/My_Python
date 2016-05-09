#coding=utf-8
'''
单下划线作前缀，意思是只有类对象和子类对象自己能访问到这些变量，
且不能用'from module import *'导入。如：
但是类里面的_还是可以用
'''
from single_ import names
from single_ import Teacher

# from single_ import _names 报错
# 用_开头的对象或者变量无法import


