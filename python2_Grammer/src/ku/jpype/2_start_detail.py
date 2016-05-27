#coding=utf-8
'''
Created on 2016年3月30日
@author: 李健博
程序作用：

'''
from __future__ import  division
import sys

import jpype 

'''
启动 JVM
JPype 提供的 startJVM() 函数的作用是启动 JAVA 虚拟机，
所以在后续的任何 JAVA 代码被调用前，必须先调用此方法启动 JAVA 虚拟机。
系统默认的JVM路径
startJVM的第一个参数是JVM库所在的路径（和JAVA_HOME不是一回事儿），
通常可以用jpype.getDefaultJVMPath()来自动获取系统默认JVM的路径。
也可以自定义路径
如果系统中安装了多个JDK，希望从中选择一个，则可以手动注明这个路径。
比如 C:\Program Files\Java\jdk1.7.0_79\jre\bin\server\jvm.dll

参数
startJVM(jvm, *args)

参数 1： jvm, 描述你系统中 jvm.dll 文件所在的路径，
如“ C:\ProgramFiles\IBM\Java50\jre\bin\j9vm\jvm.dll ”。
可以通过调用 jpype.getDefaultJVMPath() 得到默认的 JVM 路径。

参数 2： args, 为可选参数，
jpype.startJVM(vmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/home/some-lib.jar:")
会被 JPype 直接传递给 JVM 作为 Java 虚拟机的启动参数。
此处适合所有合法的 JVM 启动参数，例如：
-agentlib:libname[=options] 
-classpath classpath 
-verbose 
-Xint
 





剩下的都是发送给JVM的启动参数，每个逗号见是一个参数。
因为这里是不支持带空格的参数写法的，所以例子里特意把classpath参数写成了-Djava.class.path=...的形式。
注意这里需要手工保证参数的正确性，jpype是不会对错误的参数给出提示的，它的反应很简单，
就是在后面用到这个JVM的时候报一些怎么也想不明白的错误……所以，使用jpype遇到任何问题，
首先检查传给startJVM的各参数正确性。
'''
vmPath = jpype.getDefaultJVMPath()
jpype.startJVM(vmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/home/some-lib.jar:")
jpype.shutdownJVM()