#coding=utf-8
'''
Created on 2015年8月4日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

'''
小括号 
用法一：
在正则表达式中正则表达式匹配中只会显示小括号里面的内容

用法二：
或规则 (?: )
主要用来长字符串的或
比如a(?:123|456)b   用[123|456]的话会被认为是单个字符1,2,3,4,5,6,|

''' 

# 如果有()只显示()里面的 分组捕获
# sen='''aa456bba123aaaa'''
# lis=re.findall("aa(456)bb", sen) # aa456bb但因为(456)只显示456
# print lis # ['456']

# 怎么显示全部包括()外面的 把外面的也包起来这个会显示两个组
# sen='''aa456bba123aaaa'''
# lis=re.findall("(aa(456)(bb))", sen) 
# print lis # ('aa456bb', '456', 'bb')] 哪一个括号在前面就先显示哪一个

# 只分组不捕获(和 "?:" 一起)
sen='''aa456bba123aaaa'''
lis=re.findall("aa(?:456)bb", sen) # aa456bb但因为(456)只显示456
print lis # ['aa456bb'] 显示整个不会只显示456


# # 数量词 限定?+*
# sen='''aa456ba123aaaa'''
# lis=re.findall("(aa|bb)+", sen) # 匹配中了a456b 但是只显示456
# print lis # ['456']
# 
# # 限定|
# sen='''aa456ba123bb'''
# lis=re.findall("(123|456)", sen) # 匹配中了a456b 但是只显示456
# print lis # ['456']

# 反向引用捕获文本
'''
使用小括号指定一个子表达式后，匹配这个子表达式的文本(也就是此分组捕获的内容)
可以在表达式或其它程序中作进一步的处理。默认情况下，每个分组会自动拥有一个组号,
规则是：从左向右，以分组的左括号为标志，第一个出现的分组的组号为1，第二个为2，以此类推。
'''

# sen='''s123'''
# sen2='''s123123123'''
# lis=re.findall(r"(123)\1", sen) # 这个表达式是123123 因为第一个123匹配中了 后面的\1代表前面的123
# print lis # []
# lis=re.findall(r"(123)\1", sen2) # 匹配中了123123 但是因为(123) 所以只显示123
# print lis # ['456']

 
# # 用法二 匹配a123b和a456b
# sen='''a456ba123b'''
# lis=re.findall("a(?:123|456)b", sen) # lis中会存123和456但是忽略掉a和b
# print lis # ['a456b', 'a123b']





# sen='''http://www.baidu.com'''
# lis=re.findall("(http|ttp):", sen)
# print lis

