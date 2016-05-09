#coding=utf-8
'''
Created on 2015年6月11日
@author: Administrator
'''
#split  把字符串按空格分割为一个字符串数组
# 字符串的split函数默认分隔符是空格 ' '
# a="a b c d"
# b=a.split()
# print b # ['a', 'b', 'c', 'd']


#用特定的分隔符
# b="a-b-c-d"
# a=b.split("-")
# print a #['a', 'b', 'c', 'd']

# 关于tab split('\t')

# 拆分 |被去掉了    拆分成一个list['a', 'b', 'c']
# a = 'a|b|c'
# b=a.split('|') # |的左边右边各被拆分成一个字符串
# print b #['a', 'b', 'c']  # |被去掉了

# 有多个需要分割的目标在一起
# a = 'a|||b|c'
# # |的左边右边各被拆分成一个字符串  两个||中间会出现一个空的字符串
# b=a.split('|') 
# print b #['a', 'b', 'c']  # |被去掉了


# 要分割的在字符串的首部或者尾部
# a="|a|a|"
# b=a.split('|')
# print b #['', 'a', 'a', '']
# print len(b)


# 出现过的问题 
# sen="aspects aspects of "
# sen=sen.split(" ")
# print sen #['aspects', 'aspects', 'of', '']

# #解决办法
# sen =[s for s in sen if len(s)>0]
# print sen


