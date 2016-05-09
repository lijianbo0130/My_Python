#coding=utf-8
'''
Created on 2016年3月22日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re
re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._-]+)", re.U)


sen1=ur"aaa---aa---"
# 只包含中文  正确
re_han = re.compile(ur"[\u4E00-\u9FA5\uf900-\ufa2da-z-]+") # 1.先编译正则表达式
lis=re_han.findall(sen1)  # 开始使用findall
# 得到句子里面的所有中文
for word in lis:
    print word# 我的 我的 不包括中文英文的逗号和句号