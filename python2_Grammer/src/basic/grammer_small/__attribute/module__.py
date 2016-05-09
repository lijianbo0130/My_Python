#coding=utf-8
'''
对象或者类所在的模块
'''


class T():
    pass

t=T()

print T.__module__# __main__
print t.__module__# __main__

#从其他模块引入
from t import F
print F.__module__# t

s= F()
print s.__module__# t