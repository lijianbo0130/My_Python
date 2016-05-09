#coding=utf-8
'''
子类调用父类的方法
但是父类的对象首先就存在了
这样继承没用

也是对类的对象 出来了以后 p=Parent()
c=child(p)是错的 不能这样
'''


class Parrent():
    def __init__(self,name):
        self.name = name

class Child(Parrent):
    
    def __init__(self):
        print Parrent.name
    

p=Parrent("aa")
c=Child(p)
print c.name


