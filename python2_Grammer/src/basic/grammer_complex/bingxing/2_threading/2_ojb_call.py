#coding=utf-8
'''
变成对象
'''
import threading
from time import sleep,ctime


class ThreadFunc():
    def __init__(self,func,args,name=""):
        self.func = func
        self.args = args
        self.name = name
    
    def __call__(self):
        apply(self.func,self.args)
    


        
def loop(nloop,sec,):
    print loop.__name__+"start at"+ctime()
    sleep(sec)
    print loop.__name__+"start at"+ctime()

    
loops=[4,2]
locks=[]
nloops=range(len(loops))
threads=[]

    
for i in nloops:
    #使用对象的方式
    t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
    #加入lis
    threads.append(t)


#启动现成
for i in nloops:
    threads[i].start()
    
#检测线程是否执行完毕
for i in nloops:
    threads[i].join()

