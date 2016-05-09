#coding=utf-8
'''
Created on 2016年3月21日
@author: 李健博
程序作用：
2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode
而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的
而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。
'''
from __future__ import  division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


# 加了unicode_literals 后"" 的内容自动等于u""  b""才等于str
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)