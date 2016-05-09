#coding=utf-8
'''
不要用类对象修改类的静态成员变量
'''

#类属性为不可变元素int
class T():
    version=1
    def __init__(self,a):
        self.a = a
    

t=T("a")
print t.version# 1
t.version+=1
print t.version# 2
#对象不会改变类的静态变量 
print T.version# 1
#其实这个时候只是在对象中新定义了一个version 变量覆盖了原来的变量一旦把这个变量删除原来的变量又会出现
del t.version
print t.version# 1


# 如果为dict 一切都不同了  对象可以改变静态类成员。不存在覆盖的问题
