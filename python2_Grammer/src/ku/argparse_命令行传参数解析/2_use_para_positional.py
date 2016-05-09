#coding=utf-8
'''
Created on 2015年8月27日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
传入一个参数被echo接受 然后打印这个参数
'''
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print args.echo

'''
加入help 参数
'''
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print args.echo

'''
指定参数数据类型
type=int 默认为str
参数分两种 
一种是positional 参数接受参数的时候是按顺序接受的
调用脚本时必须输入值
参数输入的顺序与程序中定义的顺序一致
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print args.square**2