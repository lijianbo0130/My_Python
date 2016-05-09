#coding=utf-8
'''
匿名函数
'''

#简单的例子 一个参数
def f(x):
    return x**2
print f(4)

g = lambda x : x**2
#g为一个函数 会把4传给g
print g(4)


