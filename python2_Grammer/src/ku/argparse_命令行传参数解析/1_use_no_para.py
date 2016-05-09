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
使用这个包会对你在命令行输入的参数做出回应
输入:
python 1_use.py -h
输出:
usage: 1_use.py [-h]
optional arguments:
  -h, --help  show this help message and exit
  
输入没有设定的参数会报错
python 1_use.py -w
usage: 1_use.py [-h]
1_use.py: error: unrecognized arguments: -w
'''
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()


