#coding=utf-8
'''
这个是example不要乱改
'''

#encoding=utf-8
import jieba



'''
1 邮箱 307508861@qq.com
'''
seg_list = jieba.cut(ur"307508861@qq.com", cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # 307508861/ @/ qq/ ./ com

'''
2 特殊符号 @_@@%%
'''
seg_list = jieba.cut(ur"@_@@%%", cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # @/ _/ @/ @/ %/ %

'''
3 换行
如果有\n
会把\n也输出
输出 李健博/ 
/ 而已/ 
'''
s='''李健博
而已
'''
seg_list = jieba.cut(s, cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  


