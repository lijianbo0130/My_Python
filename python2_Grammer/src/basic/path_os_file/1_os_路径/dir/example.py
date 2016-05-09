#coding=utf-8
'''
Created on 2015年4月14日
@author: Administrator
'''
import os
import tempfile

#得到当前文件夹目录
# curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) )  )
# print  curpath #C:\Users\Administrator\workspace\history\src\v_grammer\os

#临时目录
print tempfile.gettempdir()
#在临时目录下的文件
# cache_file = os.path.join(tempfile.gettempdir(),"jieba.cache")
# print cache_file




#查看两个文件创建时间是否相等
# if os.path.exists(cache_file) and os.path.getmtime(cache_file)>os.path.getmtime(os.path.join(_curpath,"dict.txt")):
#     print >> sys.stderr, "loading model from cache"
#     try:
#         trie,FREQ,total,min_freq = marshal.load(open(cache_file,'rb'))
#         load_from_cache_fail = False
#     except:
#         load_from_cache_fail = True

