#coding=utf-8
'''
用多个except来捕捉
'''

b="aa"
try:   
    a=float(b)
except ValueError,reason:   
    print ValueError,reason
except TypeError,reason:   
    print TypeError,reason
finally:
    pass
    
