#coding=utf-8
'''
Created on 2016年2月22日
@author: asus-pc
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

# 不管怎么引入都会先执行全局化代码块

# 引入文件
# from w import t1
# t1.show()

# 也可以引入某个函数
# from w.t1 import show
# show()

# 但是不能 也就是import 后面只能带一个
# from w import t1.show

# 使用别名
from w.t1 import show as myshow
# 这个时候show就不能用了，只能使用myshow
# show()


