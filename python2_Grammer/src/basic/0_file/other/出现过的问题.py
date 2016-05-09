'''
1.f1=open(r'C:\Users\asus\Desktop\dataset\email\ham\%s.txt' % (2),'r',encoding= 'utf-8')
字符串开头没有加r
在Python的string前面加上‘r’, 是为了告诉编译器这个string是个raw string,不要转意backslash '\

2.文件本身的编码不对 不是utf-8
@author: asus
'''
