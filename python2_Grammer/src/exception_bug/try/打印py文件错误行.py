#coding=utf-8
'''
打印当前.py文件错误行
'''


import sys
try:
    a = [1,2]
    print a[3]
except:
    s=sys.exc_info()
    print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
