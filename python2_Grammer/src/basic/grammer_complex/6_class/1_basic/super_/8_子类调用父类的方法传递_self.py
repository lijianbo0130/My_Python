#coding=utf-8
'''
子类中调用父类的load方法 初始化子类自己
'''

#定义一个类
class Parent():
    def __init__(self,name):
        self.name = name
    
    def load(self):
        self.a="a"
        self.b="b"

#从父类继承 Child从Parent继承  继承构造方法
class Child(Parent):
    def __init__(self,name):
        #用父类的构造函数
        Parent.__init__(self, name)
        
    def load(self,s):
        #先用父类的方法
        Parent.load(self)
        self.s=s


#实例化对象
c=Child("a")
print c.name
#调用load方法
c.load("sss")
print c.a,c.b,c.s
