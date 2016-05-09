#coding=utf-8
'''
Created on 2016年2月17日
@author: asus-pc
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
\r换行 相当于回车
\n新行
.表示除了\n以外的任意字符
任意字符包括\n为 [\s\S]+
单个数字  [0123456789] \d 
非数字 \D=[^\d]
空白字符 \s  [空格|\t|\n|\r]
非空白符号 \S
单个字母 \w [A-Za-z0-9_] 包含 '_'
非单词字符 \W
'''
