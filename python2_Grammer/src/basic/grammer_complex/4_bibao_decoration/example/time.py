#coding=utf-8
'''
计算一个函数运行的时间长度
'''
import time
def timeit(func):
    #加入wrapper 是为了对func进行封装
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        end =time.clock()
        print 'used:', end - start
        return func
    #必须要返回一个变量
    return wrapper


@timeit 
def xx():
    for i in range(50):
        print i
        
     
xx()