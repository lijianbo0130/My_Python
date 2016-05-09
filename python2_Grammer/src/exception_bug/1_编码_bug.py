#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
问题
UnicodeDecodeError: ‘XXX' codec can't decode bytes in position 2-5: illegal multibyte sequence 
解答
这是因为遇到了非法字符，因此在转码的过程中出现了异常。
具体哪些字符是非法字符我也搞不清
将获取的字符串strTxt做decode时，
指明ignore，会忽略非法字符,这样就可以了
inStr2 = inStr.decode('utf-8', 'ignore')

问题
'ascii' codec can't encode character  
解答  引入  真的能解决问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

问题
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-12
解答
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
unicode 和ascii不兼容



'''