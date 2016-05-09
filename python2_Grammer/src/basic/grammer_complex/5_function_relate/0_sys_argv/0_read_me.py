#coding=utf-8
'''
sys.argv返回的是命令行的参数列表
比如你要运行一个hello.py的程序需要用命令行传入参数，比如名字
运行就是  python hello.py "张三"
那么 你可以通过 sys.argv一个列表["张三"]
然后在程序里面使用 比如输出print出来

比如
python test.py --t help --v
那么sys.argv就是['test.py', '--t', 'help', '--v']
那么sys.argv[1:]就是['--t', 'help', '--v']
'''
