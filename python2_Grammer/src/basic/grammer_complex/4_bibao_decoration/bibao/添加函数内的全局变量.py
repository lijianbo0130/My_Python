#coding=utf-8
'''
在函数中定义一个全局变量
'''

def hellocounter (name):
    #必须这样定义 不然会找不到这个变量
    count=[0] 
    def counter():
        count[0]+=1
        print 'Hello,',name,',',str(count[0])+' access!'
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()  
