#coding=utf-8
'''
1 如果自己没有定义init函数调用父类的init
2 自己定义了就不调用父类的 也无法调用父类的在init中初始化的成员
3 最好在自己的init函数中调用父类的init函数
4 子类不能定义在父类的前面
'''

#定义一个类
class Parent():
    def __init__(self,name):
        self.name = name

#从父类继承 Child从Parent继承  继承构造方法
class Child(Parent):
    def __init__(self,name):
        Parent.__init__(self,name)
        self.hh="aa"

#实例化对象
c=Child("aa")
print c.name
print c.hh