#coding=utf-8
'''
是否是某一个类型的变量
'''
print isinstance({},dict) #True
print isinstance(5,dict) #False
print isinstance([],dict) #False
print isinstance("ss",str)
a=[1,2,3]
print isinstance(a,list)
