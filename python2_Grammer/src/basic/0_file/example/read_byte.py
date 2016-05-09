#coding=utf-8
'''
Created on 2015年6月10日
@author: Administrator
'''
from __future__ import  division
#  不使用with
# file_object = open(r'data.txt', 'rb')
# 
# 
# #读取一个字节
# chunk = file_object.read(1)
# print chunk
# #读取两个字节
# chunk = file_object.read(2)
# print chunk
# #读到了末尾
# if not chunk:
#     break

# 使用with
with open(r'data.txt','rb') as somefile:
    #读取一个字节
    chunk = somefile.read(1)
    print chunk
    chunk = somefile.read(2)
    print chunk



