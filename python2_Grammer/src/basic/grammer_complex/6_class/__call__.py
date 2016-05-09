#coding=utf-8
'''
Python中的__call__允许程序员创建可调用的对象(实例)，
默认情况下 __call__()方法是没有实现的,
这意味着大多数实例是不可调用的。然而，如果在类定义中覆盖了这个方法，
那么这个类的实例就成为可调用的。
'''

class P(): 
    def __init__(self): 
        pass
   
   
p = P()
#p() 会报异常但是如果实现__call__ 方法就不会报异常

class G(): 
    def __init__(self,g): 
        self.g=g
    
    def __call__(self,t):
        return (self.g*t**2)/2
# 但是g相对于t，是一个稳定得多的数量，基本上，在一次相关运算中，g可以当作常量。
# 那么，一个可调用对象也许更适合。下面定义这样一个类型
g = G(9.8)
#实现了__call__  g可以当一个函数使用
s = g(t=1.0)
print s

