#coding=utf-8
'''
yield i   返回一个i的数列
直接用 for i in function来接受
yield 实际上没有计算 直接返回的是函数 什么时候需要计算在开始调用
'''

'''简单输出斐波那契數列前 N 个数  

问题 :    结果没有问题，但有经验的开发者会指出，
直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。'''

# 简单输出斐波那契數列前 N 个数  
# def fab(max): 
#     n, a, b = 0, 0, 1 
#     while n < max: 
#         print b 
#         a, b = b, a + b 
#         n = n + 1
# fab(5) 

'''要提高 fab 函数的可复用性，最好不要直接打印出数列，
而是返回一个 List。以下是 fab 函数改写后的第二个版本：

问题： 改写后的 fab 函数通过返回 List 能满足复用性的要求，
但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 
的增大而增大，如果要控制内存占用，最好不要用 List'''

# def fab(max): 
#     n, a, b = 0, 0, 1 
#     L = [] 
#     while n < max: 
#         L.append(b) 
#         a, b = b, a + b 
#         n = n + 1 
#     return L

'''要提高 fab 函数的可复用性，最好不要直接打印出数列，
而是返回一个 List。以下是 fab 函数改写后的第二个版本：

问题： 改写后的 fab 函数通过返回 List 能满足复用性的要求，
但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 
的增大而增大，如果要控制内存占用，最好不要用 List来保存中间结果，
而是通过 iterable 对象来迭代。'''

for i in range(1000): pass
#会导致生成一个 1000 个元素的 List，而代码：
for i in xrange(1000): pass
#则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，
#内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。


def fab(max): 
    i=0
    while i<max:
        yield i
        i=i+1
        
for n in fab(5): 
    print n 





        
