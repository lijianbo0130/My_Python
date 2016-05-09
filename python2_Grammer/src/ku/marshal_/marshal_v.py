# coding=utf-8
'''
：None、整型、长整型、浮点数、字符串、Unicode对象、元组、列表、集合、字典和code对象，
这里要求元组、列表和字典包含的值也是被支持的类型；不支持递归列表和字典（会造成无穷递归）

因为set是无序的
所以set 不能mash

list可以mash

'''

import collections as c
import marshal





# list_sen=["aaaaaab","dddddddc"]
#写入
# marshal.dump(list_sen,open("1.ms",'wb'))
#读取
# list_s = marshal.load(open("1.ms",'rb'))
# print list_s

list_sen={"a":1,"b":2};lis=[555,"sss"]
marshal.dump((list_sen,lis),open("1.ms",'wb'))
list_sen,lis = marshal.load(open("1.ms",'rb'))
print list_sen,lis
 
# list_sen=c.OrderedDict({"a":1,"b":2})  #unmarshallable object
# marshal.dump(list_sen,open("1.ms",'wb'))
# list_s = marshal.load(open("1.ms",'rb'))
# print list_s
