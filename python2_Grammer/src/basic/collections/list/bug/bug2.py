#coding=utf-8
'''
答案是函数参数的默认值只会评估使用一次—在函数定义的时候。
因此，bar参数在初始化时为其默认值（即一个空列表），
即foo()首次定义的时候，但当调用foo()时（即，不指定bar参数时）
将继续使用bar原本已经初始化的参数。
'''
def foo(bar=[]):        # bar is optional and defaults to [] if not specified
    bar.append("baz")    # but this line could be problematic, as we'll see...
    return bar

#修改
def foo_fix(bar=None):
    if bar is None:        # or if not bar:
        bar = []
        bar.append("baz")
    return bar


print foo()#['baz']
print foo()#['baz', 'baz']
print foo()#['baz', 'baz', 'baz']


def foo1(bar=""):        # bar is optional and defaults to [] if not specified
    bar+="s"  # but this line could be problematic, as we'll see...
    return bar



print foo1()#s
print foo1()#s
print foo1()#s



