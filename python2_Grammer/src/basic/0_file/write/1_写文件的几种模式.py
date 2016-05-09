#coding=utf-8
'''
Created on 2015年8月20日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


'''
w 表示 write  
以写方式打开文件，可向文件写入信息。如文件存在，
则清空该文件，再写入新内容

r 表示 read
以读方式打开文件，可读取文件信息。

b 表示 binary 最好读写都使用
以二进制模式打开文件，而不是以文本模式。
该模式只对Windows或Dos有效，
类Unix的文件是用二进制模式进行操作的。

a  一般使用ab  a默认就有w模式
以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），
如果文件不存在则创建
'''

# write 写入一个字符串没有换行
# a=["ssssss","sdsdws","sdsaaadws"]
# with open(r'1.txt','wb') as f:
#     for line in a:
#         f.write(line)

# 使用append 模式
a=["ssssss\n","sdsdws\n","sdsaaadws\n"]
with open(r'1.txt','ab') as f:
    for line in a:
        f.write(line)