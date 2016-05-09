#coding=utf-8
'''
1 import 
import只能import py文件，然后使用文件.方法 来调用方法
而不能import 文件.方法
import socket   socket为一个py文件
socket.AF_INET  AF_INET 为一个方法
直接调用  AF_INET 是找不到的

#加as 可以使用别名 不然必须使用全名
import socket as so

from socket import*是把socket下的所有名字引入当前名称空间
可以加as
from socket import pt as pt

在eclipse 中from 是从当前src文件夹下找  pydev 自动把目录加入了 python 的搜索目录 sys1.path
也可以从主目录开始找  from v_grammer.vmport.v import w
'''

'''
1 import 
而不能import 文件.方法
import只能import py文件，然后使用文件.方法 来调用方法
import socket   socket为一个py文件
socket.AF_INET  AF_INET 为一个方法
直接调用  AF_INET 是找不到的
'''
# 不能引入方法
# 报错因为 show 是一个t1文件里面的方法不能直接import
# import w.t1.show  

# 引入文件 
import w.t1
# 调用方法会执行
# t1.show() 报错 必须写全路径w.t1.show()
# a,c 第一次调用会执行全局的代码打印c，所以主方法最好写在main里面不要写在全局代码块
# w.t1.show()# ac
# w.t1.show()# a

# 使用别名
# 每次w.t1.show()很麻烦可以使用别名
from w import t1 as t
t.show()


#可以引入文件(模块)
# print w.geta()
#但是不能引入函数 报错
# import v_grammer.v_import.w.geta as get
# get()

#或者
# import v_grammer.directory_os.v_import.w 
# print v_grammer.directory_os.v_import.w.geta() #必须要加入全路径


#包 这个时候不能像导入模块一样 导入包报下面的米快会无法使用 必须在包的__init__中 import 模块
# import v_grammer.directory_os.v_import as k
#会找不到这个模块    但是如果在 k的__init__文件下面加入 import w k下面有就有了w这个模块就正常了
# print k.w.geta() 

#改为from import 
# from v_grammer.directory_os.v_import import w
# print w.geta()


# 直接import 会从sys.path()下的目录查找  在同一个目录下的文件会被搜索到
# import w
# print w.geta()


#不会有同名文件和文件夹到底引用哪个

#和系统冲突  会先搜索系统的  
# import sys
# print sys.geta()
# print sys.path








