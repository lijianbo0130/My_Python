#coding=utf-8
'''
jane=[18,man,play computer]
其中Jane[0]。但是如果tuple中的元素很多的时候操作起来就比较麻烦，有可能会由于索引错误导致出错。
我们今天介绍的namedtuple对象就如它的名字说定义的那样，你可以给tuple命名，具体用户看下面的例子
相当于定义一个类  包含一些类属性
'''
import collections


# Person = collections.namedtuple('Person', 'name age gender')
# # print  type(Person) #<type 'type'>
# bob = Person(name='Bob', age=30, gender='male')
# print  bob.name  #Person(name='Bob', age=30, gender='male')

#定义一个list对象  把list转成 namedtuple  再转成dic通过名字访问
websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

nameweb=[]
Website = collections.namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website)
    nameweb.append(website)
#     print website

dic={}
for i in nameweb:
    dic[i.name]=i
    
print dic
    



