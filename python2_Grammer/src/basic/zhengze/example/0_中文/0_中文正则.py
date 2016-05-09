#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
[\u4E00-\u9FA5\uf900-\ufa2d] 不包括中文英文的逗号和句号
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re


sen1=u"我.的a我的,。"


# 只包含中文  正确
re_han = re.compile(ur"[\u4E00-\u9FA5\uf900-\ufa2d]+") # 1.先编译正则表达式
# lis=re_han.findall(sen1)  # 开始使用findall
# # 得到句子里面的所有中文
# for word in lis:
#     print word# 我的 我的 不包括中文英文的逗号和句号
    
# 中文.a-z    正确
# re_han=re.compile(ur"([\u4E00-\u9FD5a-zA-Z0-9+#&\._]+)", re.U)
# lis=re_han.findall(sen1)  # 开始使用findall
# # 得到句子里面的所有中文
# for word in lis:
#     print word# 我的aa .我的 .... 不包括中文英文的逗号和句号
    


re_han = re.compile(ur"([\u4E00-\u9FA5\uf900-\ufa2d]+)") # 1.先编译正则表达式
blocks = re_han.split(sen1)
for block in blocks:
    print block