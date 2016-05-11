#coding=utf-8
'''
本地硬盘和u盘的读取速度可能相差50倍
'''
'''
字符串开头没有加r
如：
f1=open(r'a.txt' % (2),'r',encoding= 'utf-8')

在Python的string前面加上‘r’
是为了告诉编译器这个string是个raw string,不要转意backslash '\
'''
'''
文件一定要使用utf-8 无bom
不然读进来的文件第一行会有错误
python自动写入的文件是utf-8 无bom的
'''

