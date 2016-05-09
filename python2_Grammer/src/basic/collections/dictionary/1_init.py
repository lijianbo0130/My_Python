#coding=utf-8
'''
Created on 2015年3月8日
@author: asus
'''

# 初始化
#前面是key后面是value
dic = {"武汉":1,2:'b',3:'c'}

#长度
# print len(dic) # 有三个键值对


#是否含有key 返回True,False
# if  dic.has_key("武汉"):
#     print "Ture"
# if not dic.has_key("湖北"):
#     print "Ture"

#得到value
# print dic["武汉"]
    
#修改value
# dic[1]='aaa' #若不存在key，则添加元素
# print dic[1]


#得到所有的key  这里只能使用key这个关键字
# for key in dic:
#     print key # 3 2 武汉

# 所有的values
# print dic.values() # value的lis['c', 'b', 1]
# 所有的keys
# print dic.keys() # value的lis['c', 'b', 1]





#插入 insert(index,value)
# dic.insert(2,5)

#删除key 
# dic = {"武汉":1,2:'b',3:'c'}
# del dic["武汉"]
# print dic

#字典嵌套
# a={}
# a[u"武汉"]={}
# a['']=''
# print a

#get 方法 查看key在不在。存在会返回value,不存在返回自己定义的
# dict.get(key, default=None)
# key -- 这是要搜索在字典中的键。
# default -- 这是要返回键不存在的的情况下默认值。
# 该方法返回一个给定键的值。如果键不可用，则返回默认值为None。
dic = {'1':'first','2':'second','3':'third'}
print dic.get("1",'error')# 存在返回 value
print dic.get("x",'error')# 不存在返回 自己定义的error






#字典变成list
# freq = [(k,v/total) for k,v in freq.iteritems()]
#字典排序
# st_list = sorted(tf_idf_list,reverse=True)



# 字典拷贝
#用 dict 实际上是浅拷贝
# sos={}
# sos[0]=[1,2]
# buf=dict(sos)
# sos[0][1]=0
# print sos
# print buf

#深拷贝
# import copy
# sos={}
# sos[0]=[1,2]
# buf=copy.deepcopy(sos)
# sos[0][1]=0
# print sos
# print buf


#用赋值两个指向的还是同一个对象没有拷贝
# sos={}
# sos[0]="lijianbo"
# buf=sos
# sos[1]="lijianbo"
# print sos
# print buf


# list 不能作为key
# s=[1,2,3]
# w={s:1}
# print w

#字典作为多维数组
# a_list=['a1','a2','a3','a4',]
# dic_test={}
# for x in a_list:
#     dic_tmp={x:{}}
#     dic_test.update(dic_tmp)
# 
# 这样定义之后，对字典进行赋值
# dic_test['a2']['b3']=421
# dic_test['a4]['b2]=7482


#多个dict
# dict_pro_three={}
# list_symbol=['*', "I-GENE", 'O', 'Stop']
# for symbol1 in list_symbol:
#     dict_pro_three[symbol1]={}
#     for symbol2 in list_symbol:
#         dict_pro_three[symbol1][symbol2]={'*':0, "I-GENE":0, 'O':0, 'Stop':0}
# 
# for k1 in dict_pro_three:
#     # * Stop O I-GENE
#     for k2 in dict_pro_three[k1]:
#         for k3 in dict_pro_three[k1][k2]:
#             print k3


