#coding=utf-8
'''
findall找出字符串中所有匹配的模式
实际当中非常常用的方法
'''
import re

#两种用法 

# 1.先编译正则表达式
pattern = re.compile(r'h')
# 开始使用findall
lis=pattern.findall("hhhhh") # 返回的是一个lis
# print  lis # ['h', 'h', 'h', 'h', 'h']


'''
2.不编译直接用
a为字符串
findall(a,b)
在字符串b中找到所有能被a匹配的子串
'''
lis=re.findall(r'h', "hhhhh")# 找到所有的h
# print lis # ['h', 'h', 'h', 'h', 'h']

#3.当有多个时候从前往后匹配 这个问题实际当中不常见
lis=re.findall(r'hh', "hhhhh")# # 找到所有的hh
# print lis # ['hh', 'hh'] 从前往后只能找到两个

# 如果没有匹配中返回[] 也就是none
lis=re.findall(r'whh', "hhhhh")
# print lis # []

'''
2.不编译直接用
a为正则表达式
findall(a,b)
在字符串b中找到所有能被a正则匹配的子串
'''
lis=re.findall(".+", "123651lop")
print lis  # ['123651lop']



