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
需要指定的传入参数
--verbose 1
如果不传入输入 程序会异常
'''
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity")
# args = parser.parse_args()
# 
# if args.verbose:
#     print "verbose turned on"
    
'''
如果不想传入参数指定
action="store_true"
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print "verbosity turned on"



