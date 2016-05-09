# coding=utf-8
'''
用with就不用close了 方便一些
'''
# 和open相关
# with open('abc.txt','r') as f:
#     pass
# 
# #等价于
# try:
#     f = open('abc.txt','r')
# except:
#     pass
# else:
#     pass
# finally:
#     f.close()

'''
为了我们自己的类也可以使用with， 
只要给这个类增加两个函数__enter__, __exit__即可：
1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用
'''
# class Sample:
#     def __enter__(self):
#         print "In __enter__()"
#         return "Foo"
#  
#     def __exit__(self,type,value, trace):
#         print "In__exit__()"
#  
#  
# def get_sample():
#     return Sample()
# 
# with get_sample() as sample:
#     print "sample:",
# sample
  
 
