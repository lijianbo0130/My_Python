#coding=utf-8
'''
实际上差不多
'''

import time

def t(func):
    #加入wrapper 是为了对func进行封装
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    #必须要返回一个变量
    return wrapper

@t
def list_test():
    a=[]
    for i in range(200000000):
        a.append(i)
    return a
@t
def field_test():
    for i in range(200000000):
        yield i
        
@t 
def tt():
    #31.7
#     b=list_test()
#     for i in b:
#         print i
      
    #28.1  
#     for i in field_test():
#         print i
    pass

field_test()
print "down"
