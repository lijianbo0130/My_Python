#coding=utf-8
'''
多线程还没单线程快
如果有sleep 多线程快
'''
from __future__ import  division
import threading


class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        #初始化init
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    
    #这里改成run函数 重写了父类的函数
    def run(self):
#         print "Start",self.name,ctime()
        apply(self.func,self.args)
#         print "End",self.name,ctime()
        

def fib(x):
    if x<2: return 1
    return (fib(x-2)+fib(x-1))

def fac(x):

    if x<2: return 1
    return (x*fac(x-1))

#为了不使用系统函数sum
def summ(x):
    if x<2: return 1
    return (x+summ(x-1))


from toolkit import j_time
@j_time.timeit
def single():
    print "SINGLE THREAD"
    for i in nfuncs:
#         print "Start",funcs[i].__name__,ctime()
        funcs[i](n),
#         print "End",funcs[i].__name__,ctime()

@j_time.timeit
def combine():
    print "MULTIPLE THREAD"
    threads=[]
    for i in nfuncs:
        t=MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)
    
    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
    
    
funcs=[fib,fac,summ]*50
n=15
nfuncs=range(len(funcs))
        

combine()
single()
print "down"


