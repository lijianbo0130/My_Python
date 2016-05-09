#coding=utf-8
'''
这个时候程序是顺序执行
'''
from time import sleep,ctime

def loop1():
    print loop1.__name__+"start at"+ctime()
    sleep(2)
    print loop1.__name__+"start at"+ctime()
    

def loop2():
    print loop2.__name__+"start at"+ctime()
    sleep(2)
    print loop2.__name__+"start at"+ctime()
    
#这个时候程序是顺序执行
loop1()
loop2()
