#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

import re

#按照中文拆分句子
re_han = re.compile(ur"([\u4E00-\u9FA5]+)", re.U)
a=u"aa我来到北aa京清华大学aa我来到北aa京清华大学aa我来到北aa京清华大学"
blocks = re_han.split(a)
for i in blocks:
    print i

#只返回中文
for word in blocks:
    if re_han.match(word):
        print word
        