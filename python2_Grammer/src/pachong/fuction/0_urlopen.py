#coding=utf-8
'''
Created on 2015年6月4日
@author: Administrator
'''
import urllib
url=r"http://tu.duowan.com/m/bxgif/"

'''
urlopen
得到网页对象  urlopen(url, data, timeout)
第一个参数url即为URL，
第二个参数data是访问URL时要传送的数据，
第三个timeout是设置超时时间。
第二三个参数是可以不传送的，data默认为空None，
timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，
执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
'''
web_obj = urllib.urlopen(url)

#得到网页内容  再次读取就为空了
print web_obj.read()
#得到返回码
print web_obj.code
#返回头信息
print web_obj.headers
print web_obj.headers.values()

