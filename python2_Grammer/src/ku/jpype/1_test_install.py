#coding=utf-8
'''
Created on 2016年3月30日
@author: 李健博
程序作用：
测试jpype是否安装成功
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
如果能打印出来就证明配置成功
'''
import  jpype

# 得到jvm的路径
jvmPath=jpype.getDefaultJVMPath() 
print jvmPath
print jvmPath  # C:\Program Files\Java\jdk1.7.0_79\jre\bin\server\jvm.dll
# # 启动虚拟机
jpype.startJVM(jvmPath)
# # 是否启动
# print isJVMStarted() # True
# 
# # 调用类来输出
# java.lang.System.out.println("hello world")
# # 关闭虚拟机
# shutdownJVM()