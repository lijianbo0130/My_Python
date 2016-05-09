#coding=utf-8
'''
一个关于list的bug
'''


#bug 因为[[0] * 5] * 3 是引用复制三次  二次复制会出问题
# multi = [[0] * 5] * 3
# print  multi
# multi[0][0]=1
# print multi

#单次不会
# c=[0]*10
# print c
# c[0]=1
# print c




