#coding=utf-8
'''
Created on 2015年8月5日
@author: Administrator
'''
from __future__ import division

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


# http这种格式
sen='''=13) {window.location='http://www.yuanan.org/news/index.php?page='}'''

'''
网址的正则表达式
解读 以https?|ftp|file 开头 接 :// 多个[-A-Za-z0-9+&@#/%?=~_|!:,.;] 以[-A-Za-z0-9+&@#/%=~_|]结束
'''
pattern=re.compile("((?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|])")
lis=pattern.findall(sen)
print lis # ['http://www.yuanan.org/news/index.php?page=']

# www.baidu.com 这种格式
sen="www.baiu.com aaa.com www.aaa"
pattern=re.compile("www\..*?\.com")
lis=pattern.findall(sen)# 以se结尾
print lis  # ['se']