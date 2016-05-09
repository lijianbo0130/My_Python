#coding=utf-8
'''
私有变量 __
'''

class Teacher():
    
    def __init__(self,name):
        '''
        私有变量外部无法访问
        '''
        self.__name=name
        
    '''
    私有函数外部无法访问
    '''   
    def __get_name(self):
        print self.__name
        

        
t=Teacher("李健博")
# print t.__name # 外部使用私有变量会报错
# print t.__get_name() # 私有函数外部无法访问

