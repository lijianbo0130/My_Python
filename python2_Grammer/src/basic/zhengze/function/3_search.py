#coding=utf-8
'''
Created on 2015年5月15日
@author: Administrator
'''
import re
#search 会从整句中找到第一个适合的
# m=re.search(pattern, string, flags)  
#pattern  正则表达式   string需要匹配的句子
m=re.search("ss", "sssbbbbsss")


print m.group()  # 找到的字符串
print m.start()  # 起始位置
print m.end()  # 终止位置

# sen='''http://www.baidu.com是'''
# m=re.search("((https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|])", sen)
# print m.groups()
# print m.group()
# print m.start()
# print m.end()