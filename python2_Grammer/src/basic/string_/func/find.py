#coding=utf-8
'''
函数原型：find(str, pos_start, pos_end)

解释：

str:被查找“字串”
pos_start:查找的首字母位置（从0开始计数。默认：0）
pos_end: 查找的末尾位置（默认-1）
返回值：如果查到：返回查找的第一个出现的位置。否则，返回-1。
'''
s="aawww."
print s.find("www.") # 返回的是下标


s="我的www."
print s.find("www.") # 返回的是下标

print len("我")#非u汉字为3个字节
print len(u"我")#u汉字为1个字节