#coding=utf-8
'''
list就是一个数组 这里讲解基本用法
'''
a=[1,2,3,4,5,6]







# for 不会改变 a里面的值
# for i in a:
#     i=1
#     print i
# print a

# a=["1","2222",5,44,456]  #这个是一个个元素的匹配不会匹配元素里面的字符串
# if "22" in a:
#     print "ok" # 不存在


#append 在数组最后添加一个元素 
# a=[1,1,3]
# print(a)
# a.append(99)
# print(a) #[1, 1, 3, 99]
# a.pop()
# print a


#extend  把两个list 拼接成一个 和+号的效果一样
# a=[1,2,3]
# b=[2,3,5]
# a.extend(b) #[1, 2, 3, 2, 3, 5]
# print(a)

# +
# a=[1,2,3]
# b=[2,3,5]
# print a+b  #[1, 2, 3, 2, 3, 5]
# #a.append(b)


# 长度  显示第一个维度的长度
# a=[1,2,3,4,5,5,5,7]
# print len(a)# 8
# a=[[1,2,3],[4,5,6]]
# b=[[],[],[]]
# print len(a) #2
# print len(b) #3
# a=["sadawasd"]
# print len(a)
# print len(a[0])

# 得到转置矩阵 把行变成列
# import jb
# a=[[1,2,3],[4,5,6]]
# jb.data.print_multy_list(a) 
# c=[]
# for i in range(len(a[0])):
#     b=[example[i] for example in a]
#     c.append(b)
# #     print(b)
# jb.data.print_multy_list(c) 


    
    
#count  返回元素在列表中出现的次数。
# a=[1,1,1,2,2]
# b=a.count(a[0])
# print(b)
# c=a.count(a[3])
# print(c)

#del del用于list列表操作，删除一个或者连续几个元素。示例程序如下
# a=[1,2,3]
# del (a[0])
# print(a)



# #删除指定值的元素  一次剔除一个
# print a
# a.remove(5)
# print(a)



# 复制和乘法
#list乘法是复制不能这么使用 
#list数字中间有逗号而np.array没有
# a=[1,2,3]
#把list 复制三份
# a=a*3
# print(a) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#如果想用乘法只能转成numpy.array
# a=[1,2,3]
# import numpy as np
# a=np.array(a)
# #所有数数值乘以3
# a=a*3
# print(a)#


# 是否存在集合里
# a=[1,2,3,4,5]
# b=5
# print b in a

#insert  插入数据
# print a
# #把l插入下标为1的地方
# a.insert(1,"l")
# print a

#min
# a=min(a)
# print a

#max
# a=min(a)
# print a



# pop弹出最后一个元素
# a=[1,2,4,5]
# print a.pop() #5
# print a.pop(0) #弹出第一个元素

#多维数组初始化
# multilist = [[0 for col in range(5)] for row in range(3)]
# print multilist


#把str切开
# s="4assdwsd"
# a=list(s)
# print a



#sort
# 默认从小到大  无返回 会改变原来的大小
l=[5,3,6,8,7,2,6]
l.sort()
# l.sort(reverse=True)
print l #[2, 3, 5, 6, 6, 7, 8]

#有返回
# c=sorted()
# print c




#赋值 是传递对象   没有复制对象
# a=range(10)
# b=a
# b[5]=20
# print a
# print b

#复制对象
# a=range(10)
# b=a[:]
# b[5]=20
# print a
# print b

#越界 返回[]
# a=[1,2,3]
# b=a[4:50]
# print b

#多个空值
# c=[1]
# b=c*10
# print b
# c=[[]]
# b=c*10
# print b


#高级用法
# line="ddd ddd"
# word,freq = line.split(' ')[:2]
# print word+"1"
# print freq+"1"
# print "1","2"


#复制[]  bug
# a=[[]]*10
# print len(a)
# a[0].append(1)
# print a


#复制其他  同样bug
# a=[[1]]*10
# print a
# a[1][0]=10
# print a


# 返回多个参数
# a=[1,2,3,4,5]
# a,b,c=a[0:3]
# print a,b,c
# 
# s="1 2 3 4 5"
# a,b,c=s.split(" ")[0:3]
# print a,b,c









