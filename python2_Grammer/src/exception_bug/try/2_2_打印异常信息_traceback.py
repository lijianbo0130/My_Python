#coding=utf-8
'''
Created on 2015年7月22日
@author: Administrator
'''

    
try:   
    1/0
# 第一个表示捕获什么Exception
# 第二个参数表示异常的内容
except Exception,reason:  
    import traceback 
    traceback.print_exc()
finally:
    pass

    