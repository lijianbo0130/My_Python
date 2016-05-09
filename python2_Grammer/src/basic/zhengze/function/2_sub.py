#coding=utf-8
'''
用正则表达式实现替换功能
传统的方法能把111 替换成11 
但是无法把111 222 都替换成11
'''
import  re
# 统一空格数量  变成"a b c d"
a="a   b c  d"
# 必须要编译
p = re.compile("\s+") # 需要替换的模式
date = p.sub(' ', a) # 把字符串a里面符合p模式的字符串,替换成" "
print date# a b c d



