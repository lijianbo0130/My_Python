#coding=utf-8
'''
json 就是把数据对象变成str  在内存中
'''
import json 

#dumps 和 loads都是在内存中

# dumps 把list 对象变成json对象
# data = [{'a':"A",'b':(2,4),'c':3.0}] #list对象 
# print type(data)
# data = json.dumps(data)
# print type(data)# str json把数据变成str
# print data # [{"a": "A", "c": 3.0, "b": [2, 4]}]

# dict
# data={'a':"A",'b':(2,4),'c':3.0}
# data = json.dumps(data)
# print data # {"a": "A", "c": 3.0, "b": [2, 4]}


#loads把josn(str) 对象变成原来的对象
#如果其编码本身是非UTF-8的话，比如是GB2312的 指定编码
#dataDict = json.loads(dataJsonStr, encoding="GB2312");


# data = [{'a':"A",'b':(2,4),'c':3.0}] #list对象 
# print type(data) # list
# data = json.dumps(data)
# print type(data)# str json把数据变成str
# data=json.loads(data) #  转成原来的list
# print type(data) # list

# 编码
# json.dumps在默认情况下，对于非ascii字符生成的是相对应的字符编码，而非原始字符，例如：
# 
# >>> import json
# >>> js = json.loads('{"haha": "哈哈"}')
# >>> print json.dumps(js)
# {"haha": "\u54c8\u54c8"}
# 
# 解决办法很简单:
# 
# >>> print json.dumps(js, ensure_ascii=False)   
# {"haha": "哈哈"} 






