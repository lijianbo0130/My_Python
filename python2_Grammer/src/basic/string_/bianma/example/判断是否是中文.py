#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

import re

#u不能掉
f=u"我"
b=re.findall(ur"[\u4e00-\u9fa5]+",f)
if b==[]:
    print "不是中文"
else:
    print "是中文"

