#coding=utf-8
'''
Created on 2016年3月28日
@author: 李健博
程序作用：
这里介绍read的三种常用的方式
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')# @UndefinedVariable

#===============================================================================
# open
#===============================================================================
'''
f＝open(filename,访问方式[r,w,a,b])    
## r:读操作；w：写操作；a:添加操作；b:二进制存取
'''


#===============================================================================
# read
#===============================================================================
'''
f.read() 每次读取整个文件，
它通常将读取到底文件内容放到一个字符串变量中，返回
也就是说 f.read() 生成文件内容是一个字符串类型
用for line in f.read() 不会返回一行一行而是返回整个文件中的一个一个的字符
所以f.read很少用
'''
# fname=r"test.txt"
# f=open(fname,"rb")
# s=f.read()
# for line in s :# 会读取一个一个的字符
#     print line

#===============================================================================
# readline()
#===============================================================================
'''
f.readline() 每次只读取一行，
通常比 .readlines() 慢得多。
仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline() 
很常用因为我经常读大数据
'''

fname=r"test.txt"
f=open(fname,"rb")
line=f.readline() # 只读取了一行
while line: # 所以要用while循环 就换有换行符也会继续
    print line.strip()
    line=f.readline()

#===============================================================================
# readlines
#===============================================================================
'''
readlines 
一次全部读出来
'''
# f1=open(r'C:\Users\asus\Desktop\dataset\74975025.txt','r')
# lines=f1.readlines()
# for  line in lines : 
#     print  line.strip()


        
    

 





