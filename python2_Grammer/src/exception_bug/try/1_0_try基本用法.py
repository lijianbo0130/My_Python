#coding=utf-8
'''
基本用法
'''



try:   
    1/0  #出了异常后面的代码不会继续执行
    print "出了异常后面的代码不会继续执行"
except:   
    print "有异常才执行"  
finally:
    print "有没有异常都执行"