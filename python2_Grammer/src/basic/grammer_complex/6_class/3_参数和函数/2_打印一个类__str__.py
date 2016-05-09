#coding=utf-8
'''
重载__str__() 方法
'''

class peo:
    #下面是类的__doc__注释 '''''', 和'' ,''''都行
    '''get c2c'''
    def __init__(self,name):
        self.Name = name
        
    # 告诉程序print 类对象的时候 打印出什么
    def __str__(self):
        msg='my name is: ' +self.Name
        return msg
 
zhangsan=peo("zhangsan")
print zhangsan
