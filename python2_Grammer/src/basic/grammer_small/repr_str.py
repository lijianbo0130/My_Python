#coding=utf-8
'''
Python 有办法将任意值转为字符串：将它传入repr() 或str() 函数。
也就是说 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。
很多情况下这三者的输出仍然都是完全一样的。
'''

s = 'Hello, world.'
print s
#这种使用+号会报错
x = 10 * 3.25
y = 200 * 200
print 'The value of x is ' + str(x)

#区别 repr 和 str  repr让机器懂  str让人懂
hello = 'hello, world\n'
hellos1 = repr(hello)
hellos2=str(hello)
print hellos1
print hellos2

# repr()的对象是任意python对象
x = 10 * 3.25
# repr((x,  ('eggs'))) # "(32.5 ('spam'))"
