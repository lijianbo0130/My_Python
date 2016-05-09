#coding=utf-8
'''
s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
'''

#  当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
# b=a.strip() b改变 a不改变
# a = '     123'
# b=a.strip()
# print b  # 123

# 开头处  有多个一起去除
# a='\t\tabc'
# b=a.strip()
# print b # abc

# 结尾处
# a = 'sdff\r\n\n\n\n'
# b=a.strip()
# print b # sdff


# strip('21')  使用后不能以21开头 不能以21结尾
# a = '123abc'
# b=a.strip('21')
# print b # '3abc'   
# b=a.strip('12')
# print b # '3abc'

# 如果使用后为""
b="\t"
print len(b)# 1
b=b.strip()# ""
print len(b)# 0

