#coding=utf-8
'''
Created on 2015年6月15日
@author: Administrator
'''
#把str字符串按照任意进制转化为10进制

print int("1001",2) # 9
print int("1001",10) # 1001
print int("1001",11) # 1332


#把10进制转成16进制 返回str
print hex(10) # 0xa 返回str
print type(hex(10)) # str
#把任意进制转为2进制
print bin(0xa) # 0b1010
#把10进制转成8进制 返回str
print oct(8) # 010






