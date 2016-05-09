#coding=utf-8
'''
意思就是把\w \W \s \S等这些元字符按照 Unicode 的标准来考虑。举个例子
pattern = re.compile(ur"a\s+b", re.U)
m = pattern.findall(u"dsadadsada\u3000b") # 匹配成功
pattern = re.compile(ur"a\s+b")
m = pattern.findall(u"dsadadsada\u3000b") # 匹配失败
\u3000是中文下的unicode空格符，如果不加 re.U \s指认 ascii 中的空白符。
a　b 中间那个就是中文空格，可以用来在贴吧里缩进代码噢。
可以理解为加了re.U增加对unicode的识别
'''
import re

pattern = re.compile(ur"a\s+b", re.U)
m = pattern.findall(u"dsadadsada\u3000b") # 匹配成功
print m
pattern = re.compile(ur"a\s+b")
m = pattern.findall(u"dsadadsada\u3000b") # 匹配失败
print m
