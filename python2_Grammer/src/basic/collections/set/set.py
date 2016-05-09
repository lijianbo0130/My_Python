#coding=utf-8
'''
python的set和其他语言类似, 是一个无序不重复元素集,
基本功能包括关系测试和消除重复元素. 元素顺序排列不是按照指定顺序
集合对象还支持union(联合), 
intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.  
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合,
sets不记录元素位置或者插入点。因此,sets不支持 indexing, slicing,
 或其它类序列（sequence-like）的操作。
'''
#创建一个set  字符串会被解析成一个个字母
s1 = set("qiwsir")  
# print(s1)      #set(['q', 'i', 's', 'r', 'w'])   

# 创建一个空set     
# set1=set()


#通过list创建set.重复元素会被忽略,元素可以是int/str
#元素顺序排列不是按照指定顺序
# s2 = set([123,"google","face","book","facebook","book",123])   
# print(s2) #set(['facebook', 123, 'google', 'book', 'face'])
                

#通过{}直接创建
# s3 = {"facebook",123} 
# print(s3)    


# 元素不能包含list  set dict
# s3 = {[1,2,'a']}
# b={}#是dic
# s3 = {"a",b}
# s3={{"a"}}


#和dic的区别
# a={"a"}#是set
# b={}#是dic
# print(type(a))
# print(type(b))

# 是否为子集合
# a={1,2,3,4}
# b={1,2}
# print b.issubset(a) 
 
# 添加一项  
# a={1,2,3,4}
# print a
# a.add('x')              
# print a

#添加多项
# a={1,2,3,4}
# a.update([10,37,42])
# print a

# 测试 x 是否是在s里面
# s=set([1,2,3])
# x=1
# print x in s  
  
# 测试 x 是否是不在s里面
# print x not in s   

#遍历
# for i in s1:
#     print s1

#元素个数
# len(s) 集合基数: 集合s 中元素的个数









