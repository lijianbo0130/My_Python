#coding=utf-8
'''
Created on 2015年6月15日
@author: Administrator
'''

class peo():
    #初始化参数
    #下面是类的__doc__注释 '''''', 和'' ,''''都行
    '''get c2c'''
    def __init__(self,lis):
        self.name = lis[0]
        self.age = lis[1]
        self.sex = lis[2]

lis=[1,2,3]
s=peo(lis)
print s.age


class Peo():
    #初始化参数
    #下面是类的__doc__注释 '''''', 和'' ,''''都行
    '''get c2c'''
    def __init__(self,lis):
        self.__name = lis[0]
        self.__age = lis[1]
        self.__sex = lis[2]

lis=[1,2,3]
s=peo(lis)
print s.__age


