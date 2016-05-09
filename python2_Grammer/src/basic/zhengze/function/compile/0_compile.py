#coding=utf-8
'''
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 第二个参数flag是匹配模式，取值可以
使用按位或运算符'|'表示同时生效，比如re.I | re.M。另外，你也可以在regex字符串中指定模式，比如re.compile('pattern', r
e.I | re.M)与re.compile('(?im)pattern')是等价的。
可选值有：
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式
是等价的：


个人理解有的时候正则表达式非常长所以用
compile方法得到一个对象这样再次使用的时候直接使用对象就好
'''

import re
# 将正则表达式编译成对象才能使用
pattern = re.compile(r'lijianbo')

#  使用findall方法找到所有匹配的
s="lijianbo0130qqdddsdwdsasdlijianbo"
lis=pattern.findall(s) # 返回的是一个lis
print  lis # ['lijianbo', 'lijianbo']
    
    
    
    
    
    
    
    
    