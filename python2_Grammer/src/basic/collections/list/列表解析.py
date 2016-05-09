#coding=utf-8
'''
列表解析
列表解析在一个序列的值上应用一个任意表达式，将其结果搜集到一个新的列表中返回
'''

#所有值加2
# print [x+2 for x in range(5)]

#两个参数  把两个lis的数据相加
# print [x+y for x in [2,3,4,5] for y in [5,58,6,9]]

#带有if
# w=[1,2,3,4,4]
# print [x+2 for x in w if x>3]

#是迭代器所以不会出问题  过程中会锁死f
# f=["asdasd","ddd","dws","xls"]
# f=[x for x in f if "xls" in  x]
# print f


# 一个用法
# sen="aspects aspects of "
# sen=sen.split(" ")
# print sen #['aspects', 'aspects', 'of', '']
# sen =[s for s in sen if len(s)>0]
# print sen


# sen='''* * D N V D N Stop
# * * D N V D N Stop'''
# list_sentence=[se.split(" ") for se in sen.split("\n")]
# print list_sentence," s"

