'''
np.sort() 函数总是返回一份拷贝，而 .sort() 方法则会更改原数组。 
方法可用于给数组在指定轴向上排序。比如一个 （4，3，2）的数组，
它的对应轴向分别为（2，1，0），方法默认的 axis=-1
'''

import numpy as np



# a=np.mat([[6, 7, 1, 6], 
#        [1, 0, 2, 3], 
#        [7, 8, 2, 1]]) 
# print(a)
# a.sort()
# print(a)
# a.sort(0)
# print(a)

# 一维数组  
x = np.array([3, 1, 2])
#不改变x
a=np.sort(x)
print(x)
print(a)
#改变x
x.sort()
print(x)



#二维数组按列排序;  arr.sort(1)  #二维数组按行排序;


x = np.array([[0, 3], [2, 1]]) 
a=np.sort(x, axis=0) #按列排序
print(a)

 
a=np.sort(x, axis=1) #按行排序
print(a)
