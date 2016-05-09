#coding=utf-8
'''
第一个多线程程序
'''
import thread
from time import sleep,ctime

def loop1():
    print loop1.__name__+"start at"+ctime()
    sleep(1)
    print loop1.__name__+"start at"+ctime()
    

def loop2():
    print loop2.__name__+"start at"+ctime()
    sleep(0.5)
    print loop2.__name__+"start at"+ctime()
    
#这个时候程序是顺序执行  第一个参数是函数名  第二个参数是函数的变量
thread.start_new_thread(loop1, ())
thread.start_new_thread(loop2, ())
#如果不加sleep(5) 主现成就会结束 关闭两个进程
sleep(5)

