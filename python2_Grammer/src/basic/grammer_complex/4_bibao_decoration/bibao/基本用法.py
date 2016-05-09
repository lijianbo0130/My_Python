#coding=utf-8
'''
简单说,闭包就是根据不同的配置信息得到不同的结果
'''

def make_adder(addend):
    #把整个函数包起返回
    def adder(augend):
        print " adder 1"
        return augend + addend
    return adder
# 这个时候不会执行 print "1"  而是返回一个函数
p = make_adder(23)
# 这个时候才是调用函数
print p(100)

