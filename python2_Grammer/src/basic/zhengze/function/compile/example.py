#coding=utf-8
'''
Created on 2015年5月15日
@author: Administrator
'''

import re 
# re.U增加对unicode的识别能力
# r表示raw u表示unicode
re_eng = re.compile(ur'[a-zA-Z0-9]',re.U)

s=r"\s"
print s
s=u"s"
print s
s=ur"\s"
print  s