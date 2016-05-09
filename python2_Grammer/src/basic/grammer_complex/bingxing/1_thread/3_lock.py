#coding=utf-8
'''
加入现成锁
'''
import thread
from time import sleep,ctime

loops=[4,2]
def loop(nloop,sec,lock):
    print loop.__name__+"start at"+ctime()
    sleep(sec)
    print loop.__name__+"start at"+ctime()
    #把锁打开
    lock.release()
    

locks=[]
nloops=range(len(loops))
for i in nloops:
    #得到一个线程锁
    lock=thread.allocate_lock()
    #把锁锁上
    lock.acquire()
    locks.append(lock)
    
for i in nloops:
    thread.start_new_thread(loop, (i,loops[i],locks[i]))
    
for i in nloops:
    #如果锁没有锁上
    while locks[i].locked():
        pass
