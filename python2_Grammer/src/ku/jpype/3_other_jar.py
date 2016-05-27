# coding=utf-8
'''
Created on 2016年5月24日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys

import jpype 
jvmPath = jpype.getDefaultJVMPath() 
'''
外部jar包的路径 这里是jar包的绝对路径 多个可以设置为  a.jar;b.jar
jar文件要加入jar的全路径。加入文件路径。会被当成根目录，回会去里面找.txt文件
'''
# 
# 如果有其他的文件路径也可以加入，这里会被当成工程的根目录加进去。可以存放.txt文件
jvmArg = r"-Djava.class.path=D:\code_4_13\Python3\Python3_Main_Grammer_RM\jar\testFileDir-0.0.1-SNAPSHOT.jar"
# 把jar包加入jvm启动的路径
# 启动jvm
jpype.startJVM(jvmPath, jvmArg)
print (jpype.isJVMStarted()) # True
# 启动类  打开jar包看 ReadFile对应的是ReadFile.class文件
javaClass = jpype.JClass('com.hacksc.testFileDir.ReadFile') 
# 得到一个实例
javaInstance = javaClass() 
javaInstance.showDir()
 


 
