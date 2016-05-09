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
    import sys 
    info=sys.exc_info()  
#     print info
    print info[0],":",info[1] # [0]表示异常类型 [1]表示错误的原因
    print info[2].tb_lineno # 打印行
finally:
    pass

    