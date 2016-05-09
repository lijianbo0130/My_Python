#coding=utf-8
'''
返回一个lambda表达式
'''

#返回的为一个函数
def func():
    x=4
    action=(lambda n:x**n)
    return action

#这个时候没有参数
x=func()
#但是调用的时候要加参数
print x(4)
