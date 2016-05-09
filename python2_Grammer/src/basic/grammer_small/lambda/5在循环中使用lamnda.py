#coding=utf-8
'''
在循环中使用lamnda
如果lambda嵌套在一个循环之中，而且引用了上一次作用域的变量，该变量被循环所改变
所有在这个循环中产生的函数会有相同的值，在最后一次循环中完成时被引用的变量的值
原因： 
嵌套域中的变量在嵌套的函数被调用时才进行查找，所以他们实际上记住的是同样的值
在最后一次循环中变量的值
'''


# def makeActions():
#     act=[]
#     for i in range(5):
#         act.append(lambda x: i**x)
#     return act
# act=makeActions()
# print act[0](2)
# print act[1]

# 例子二
# fs = [(lambda n: i + n) for i in range(10)]
# 
# print fs(4)
# # print fs[3](4)
# # print fs[4](4)

#修改
# fs = [(lambda n,i=i: i + n) for i in range(10)]
#   
# print fs[3](4)
# print fs[4](4)



