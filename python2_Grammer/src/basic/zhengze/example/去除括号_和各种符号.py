#coding=utf-8
'''
Created on 2015年5月20日
@author: Administrator
'''

import re
#贪婪模式   但是这样会有问题   (a)wdwdwdsasdwad(b) 会当成(*)中间的所有的数据都被去除
txt=u".......。。。a" #去除[] 【】() （）. 。
txt = re.sub(u"\[.*\]|【.*】|\（.*\）|\(.*\)|\.|。", " ", txt)
print txt
txt=txt.split(" ")
print txt

#但是这样会有问题
txt=u"(a)wdwdwdsasdwad(b)" #去除[] 【】() （）. 。
txt = re.sub(u"\[.*?\]|【.*?】|\（.*?\）|\(.*?\)|\.|。", " ", txt)
print txt
txt=txt.split(" ")
print txt
