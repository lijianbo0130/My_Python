#coding=utf-8
'''
用装饰器打印函数的名字
'''

def dec(fun):
    print fun.__name__
    return fun#这里返回函数让别人调用

@dec
def rx(x,y):
    return x+y,x*y

x,y=rx(5,8)#这个函数先执行 fun.__name__ 然后执行 return fun 等于rx(5,8)
print x,y