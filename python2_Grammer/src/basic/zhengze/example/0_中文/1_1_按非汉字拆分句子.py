#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

import re
#按照中文拆分句子

a=u"aa我来到北aa京清华大学aa我来到北aa京清华大学"

# 小括号不能去掉 本来split的时候是去掉汉字的但是加了()里面的汉字会保存下来
re_han = re.compile(ur"([\u4E00-\u9FA5]+)") 
blocks = re_han.split(a) # 按照中文分割
for word in blocks:
    print word, # aa 我来到北 aa 京清华大学 aa 我来到北 aa 京清华大学 



        