#coding=utf-8
'''
python中用+进行字符串连接的方法效率极其低下，
其根源在于python的PyStringObject对象是不可变对象，
这就意味着当字符串连接时必须重新创建对象，重新申请内存。 
官方说法是通过join操作来存储list或者tuple的一组PyStringObject对象，
这种方法只分配一次内存。
'''
# 把list和generate里面的字符连接起来

# list
# a=["a","b","b"]
# print "".join(a) #abb
# print " ".join(a) # a b b

# generate  不过generate自能用一次
# def f(x):
#     for i in x:
#         yield i
#        
# # 把a转成一个generate     
# a=["a","b","b"]
# b=f(a)
# print b
# print "".join(b) #abb
# print " ".join(b) # a b b

