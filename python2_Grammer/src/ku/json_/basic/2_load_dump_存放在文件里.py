#coding=utf-8
'''
读到了json数据  写到文件里面
'''
import json

# 读取
data_list = json.load(open('1.txt', 'rb'))
print type(data_list)# list格式
for data_sub in data_list:
    print data_sub

# 写入
list_json=[{"name":"li"},{"name":"li2"},{"name":"li3"}]
# json.dump(list_json, open('1.txt', 'wb'))
# print "down"

# 分开写入
with open('2.txt', 'w') as f:
    f.write(json.dumps(list_json))










