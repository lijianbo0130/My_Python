#coding=utf-8
'''
操作 平均情况 最坏情况 
x in s O(1) O(n) 
并集 s|t O(len(s)+len(t))  
交集 s&t O(min(len(s), len(t)) O(len(s) * len(t)) 
差集 s-t O(len(s))  
s.difference_update(t) O(len(t))  
对称差集 s^t O(len(s)) O(len(s) * len(t)) 
s.symmetric_difference_update(t) O(len(t)) O(len(t) * len(s))

由源码得知，求差集（s-t，或s.difference(t)）
运算与更新为差集（s.difference_uptate(t)）运算的时间复杂度并不相同！
前者是将在s中，但不在t中的元素添加到新的集合中，因此时间复杂度为O(len(s))；
后者是将在t中的元素从s中移除，因此时间复杂度为O(len(t))。因此，使用时请留心，
根据两个集合的大小以及是否需要新集合来选择合适的方法。
集合的s-t运算中，并不要求t也一定是集合。只要t是可遍历的对象即可。

 
'''
