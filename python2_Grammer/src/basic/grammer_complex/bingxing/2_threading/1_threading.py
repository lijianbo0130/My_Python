#coding=utf-8
'''
threading有比较好的进程管理 不用手动lock.release()
'''
import threading
from time import sleep,ctime

loops=[4,2]
def loop(nloop,sec,lock):
    print loop.__name__+"start at"+ctime()
    sleep(sec)
    print loop.__name__+"start at"+ctime()

    

locks=[]
nloops=range(len(loops))
threads=[]

    
for i in nloops:
    #分配线程
    t=threading.Thread(target=loop, args=(i,loops[i],locks[i]))
    #加入lis
    threads.append(t)


#启动现成
for i in nloops:
    threads[i].start()
    
#检测线程是否执行完毕
for i in nloops:
    threads[i].join()

