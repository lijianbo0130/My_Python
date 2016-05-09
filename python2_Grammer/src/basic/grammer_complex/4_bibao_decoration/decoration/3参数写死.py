#coding=utf-8
'''
有参数的函数包装
'''

def deco(func):
    def _deco(a, b):
        print("before")
        ret = func(a, b)
        print("after")
        return ret
    return _deco

@deco
def myfunc(a, b):
    return a + b

s=myfunc(1, 2)
print s
