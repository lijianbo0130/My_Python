#coding=utf-8
'''
只从字符串的开始与正则表达式匹配
比如match=re.match('ss',"aassaasss") 因为第一个词是a不是s所以匹配不中
因为只能从头开始匹配所以实际当中不常用
'''

import re
# re.match(pattern, string, flags)  有两种使用方法
# pattern 可以是一个re 编译的正则表达式 或者直接用正则表达式
# 只从字符串的开始与正则表达式匹配  所以只返回一个

# 直接使用字符串作为正则表达式 从头开始找
match=re.match('ss',"ssaassaasss")
if match is not None:
    print match.group() # ss

#中文不加u会无法匹配    
match=re.match(u'中', u"中国")
if match is not None:
    print match.group()
    
    

# 使用正则表达式
# pattern = re.compile(r'h')
# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match('hello hrld!')
# if match:
# # 使用Match获得分组信息
#     print match.group() #h