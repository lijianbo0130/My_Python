# coding=utf-8
'''
Created on 2016年5月10日
@author: 李健博
程序作用：

'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import jieba

jieba.set_dictionary('data/dict.txt.big')