#coding=utf-8
'''
返回多个参数
'''
import time

def timeit(func):
    #加入wrapper 是为了对func进行封装
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        end =time.clock()
        print func.__name__,'function use' ,end - start
        return func
    #必须要返回一个变量
    return wrapper

@timeit
def x():
    x1=1
    x2=2
    x3=3
    return x1,x2,x3

x1,x2,x3=x()