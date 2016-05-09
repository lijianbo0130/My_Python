#coding=utf-8
'''
问题 
TypeError: 'int' object has no attribute '__getitem__'
解答
print t[0]  实际上当时t是一个int 类型就会出这个问题

问题
ValueError: could not convert string to float: 
解答
b=""  b不是一个数字
c=float(b)

问题 
TypeError: 'set' object is not callable  
解答 ：
b=set([1,2,3]) for i in b(): 这里不应该加()

问题
Was expecting one of:     <EOF>      <NEWLINE> ...     "(" ...   
解答 ：
没有按照python的习惯对齐 即使是注释也要对齐

问题
TypeError: first arg must be callable
thread.start_new_thread(loop1(), ())
解答
多线程的时候不要加() thread.start_new_thread(loop1, ())

问题
Unhandled exception in thread started by 
解答
在多线程中 主线程结束了 但是子进程还在运行

问题
TypeError: cannot concatenate 'str' and 'int' objects
解答
把str+int
前面是字符串后面是数字

问题
TypeError: unsupported operand type(s) for +: 'int' and 'str'
解答
int+str
前面是数字后面是str

问题
TypeError: 'int' object is not callable
解答
print len(data)  
自己定义了一个int 对象叫len 所以len这个对象不能用函数调用

问题
AttributeError: 'NoneType' object has no attribute
解答
表示None这个对象没有属性标签

问题
TypeError: expected a character buffer object
解答
write方法的实参需要为string类型



问题
MemoryError
解答
是32位的问题，使用64位的python就可以了.
32位的python内存只能用2G左右

'''
