# coding=utf-8

import redis
import chardet

r = redis.Redis(host='10.95.130.184', port=6379, db=0)  # 如果设置了密码，就加上password=密码

#插入key value
# r['wo'] = int(6)

#得到数据
# print r.get('wo') 

#r.dbsize()   #库里有多少key，多少条数据 
# print r.dbsize()

#得到所有的key
# keys = r.keys()
# print keys

#得到所有的和key对应的value
# keys = r.keys()
# vals = r.mget(keys)
# print vals

#得到所有的key value对
# keys = r.keys()
# vals = r.mget(keys)
# kv = zip(keys, vals)
# for i in kv:
#     print i

#清空
# r.flushdb()   #删除当前数据库的所有数据
# print r.dbsize()

