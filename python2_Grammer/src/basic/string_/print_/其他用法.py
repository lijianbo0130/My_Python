#coding=utf-8


import sys

# 把这句话写入到系统错误文件里面
# import sys
# print >> sys.stderr, "Trie has been built succesfully."


'''sys.stdout 与 print
当我们在 Python 中打印对象调用 print obj 时候，事实上是调用了 sys.stdout.write(obj+'\n')
print 将你需要的内容打印到了控制台，然后追加了一个换行符
print 会调用 sys.stdout 的 write 方法
以下两行在事实上等价：'''
# import sys
# sys.stdout.write('hello'+'\n') 
# print 'hello'

'''sys.stdin 与 raw_input
当我们用 raw_input('Input promption: ') 时，事实上是先把提示信息输出，然后捕获输入
以下两组在事实上等价：'''
# import sys
# hi=raw_input('hello? ') 
# print 'hello? ', #comma to stay in the same line 
# hi=sys.stdin.readline()[:-1] # -1 to discard the '\n' in input stream


'''从控制台重定向到文件
原始的 sys.stdout 指向控制台
如果把文件的对象的引用赋给 sys.stdout，那么 print 调用的就是文件对象的 write 方法'''
f_handler=open('out.log', 'w') 
sys.stdout=f_handler 
print 'hello' #直接写入到文件
# this hello can't be viewed on concole 
# this hello is in file out.log

'''记住，如果你还想在控制台打印一些东西的话，最好先将原始的控制台对象引用保存下来，
向文件中打印之后再恢复 sys.stdout复制代码'''
# __console__=sys.stdout 
# # redirection start # 
# ... 
# # redirection end 
# sys.stdout=__console__