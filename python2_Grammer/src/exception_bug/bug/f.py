#coding=utf-8
'''
Created on 2015年4月16日
@author: Administrator
'''
def create_multipliers():
    return [lambda x : i * x for i in range(5)]
for multiplier in create_multipliers():
    print multiplier(2)