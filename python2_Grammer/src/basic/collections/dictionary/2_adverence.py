#coding=utf-8
'''
Created on 2015年7月17日
@author: Administrator
'''
'''
要注意的地方:

# 不要使用dict dict为关键字
# print type(dic)  #dict 所以不要用dict这个词

# 一般都是通过key找value 通过找key想法不对因为 value不是唯一的值
'''

# dict 为无序的  根据某种算法来排序
# print dic #{3: 'c', 2: 'b', '\xe6\xad\xa6\xe6\xb1\x89': 1} 
# for key in dic:
#     print key #3 2 武汉 和存入顺序不一样

# 如果要有序用要一样用orderedDict


# key values 生成一个(key,value)对的list
# dic={1:"a",2:"b"}
# print dic.items()#  [(1, 'a'), (2, 'b')]


# key value互换
# d1={'a':1,'b':2}
# b=dict((value,key) for key,value in d1.iteritems())
# print b


