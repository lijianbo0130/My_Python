#coding=utf-8
'''
显示一个对象有哪些可以使用的方法
'''



import urllib2
# print dir(urllib2)


class Person(object):
    def __dir__(self):
        return ["name", "age", "country"]



print dir(Person)
tom = Person()
#调用对象的dir 方法
print dir(tom)
