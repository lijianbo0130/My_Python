#coding=utf-8
'''
可以用in这个操作  
可以不加u 或者同时加u
'''


if u"用" in u"用的" : #可以
    print True 

# if u"用" in "用的" :#会报 exception
#     print True


if "aa" in u"aaaa": #可以
    print True
    
if u"aa" in "aaaa": #可以
    print True
    
    
    