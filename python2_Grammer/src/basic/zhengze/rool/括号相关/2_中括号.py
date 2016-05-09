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
字符集类
如 [a-c]和[abc]表示 a或b或c
在[]中|不表示或
[]. 不表示任意字符 但是\s
^在第一个字符表示取反
'''


# 匹配 'afd', 'acd', 'a|d'
sen='''afdacda|d'''
lis=re.findall("a[fc|]d", sen) # 中间为f或c或|  在[]中|不表示或
print lis # ['afd', 'acd', 'a|d']

# ^在第一个字符表示取反
# 匹配 a开头d结尾的字符串 中间不能为a 
sen='''asdaad'''
lis=re.findall("a[^a]d", sen) # 中间为f或c或|  在[]中|不表示或
print lis # ['asd']





