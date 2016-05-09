#coding=utf-8
'''
Created on 2015年4月21日
@author: Administrator
'''
'''
转换类型          含义
d,i                 带符号的十进制整数
o                   不带符号的八进制
u                   不带符号的十进制
x                    不带符号的十六进制（小写）
X                   不带符号的十六进制（大写）
e                   科学计数法表示的浮点数（小写）
E                   科学计数法表示的浮点数（大写）
f,F                 十进制浮点数
g                   如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
G                  如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
C                  单字符（接受整数或者单字符字符串）
r                    字符串（使用repr转换任意python对象)
s                   字符串（使用str转换任意python对象）
'''

#基本使用
# strHello = 'Hello World'
# print (strHello)

#带有参数  s字符串  d十进制数字
# strHello = "the length of %s is %d" %('Hello World',len('Hello World'))
# print (strHello)

# s="123"
# x = len(s)  
# print("The length of %s is %d" % (s,x))  

#不换行 在数据后面加一个,  但是会在后面加一个空格  
# print "a","b" #a b
# print "a",
# print

#多个输出 变量和字符串一起输出
# s1=5
# s2=6
# print "s1=",s1
# print "s1=%d s2=%d"%(s1,s2)
# print "s1=%d"%s1