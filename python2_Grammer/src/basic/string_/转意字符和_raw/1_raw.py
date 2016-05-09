#coding=utf-8
'''
加了r""以后就成了Raw String 
顾名思义就是（除了结尾的反斜杠）不会被转义的字符串
'''

import re

# 转意 r""里面的\不会被转意
# 不能以 \"结尾  \后面的" 会因为\的原因不视为最终的结尾符号
# print r"\" 报错 
# a=r"\\\\"
# print a # \\\\ \没有被转义


# 想要在字符串中匹配\
# "\\\\"其实表示的是 \\ \\正则编译以后为\
# reObj = re.compile("\\\\") 
# b= reObj.findall("\\a\\b")
# print b

# 使用raw string 完成同样的事情
# 想要在字符串中匹配\
# "\\\\"其实表示的是 \\ \\正则编译以后为\
# reObj = re.compile(r"\\") 
# b= reObj.findall(r"\a\b")
# print b








