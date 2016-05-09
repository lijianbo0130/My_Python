#coding=utf-8
'''
有任意参数的函数包装
'''

def deco(func):
    def _deco(*args, **kwargs):
        print("before"+func.__name__)
        ret = func(*args, **kwargs)
        print("after"+func.__name__)
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    return a+b
 
@deco
def myfunc2(a, b, c):
    return a+b+c
 
print myfunc(1, 2)
print myfunc2(1, 2, 3)
