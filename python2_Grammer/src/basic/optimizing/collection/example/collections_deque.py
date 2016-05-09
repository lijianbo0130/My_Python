#coding=utf-8
'''
deque （double-ended queue，双向队列）是以双向链表的形式实现的 
(Well, a list of arrays rather than objects, for greater efficiency)。
双向队列的两端都是可达的，但从查找队列中间的元素较为缓慢，增删元素就更慢了。
操作 平均情况 最坏情况 
复制 O(n) O(n) 
append O(1) O(1) 
appendleft O(1) O(1) 
pop O(1) O(1) 
popleft O(1) O(1) 
extend O(k) O(k) 
extendleft O(k) O(k) 
rotate O(k) O(k) 
remove O(n) O(n) 
'''
