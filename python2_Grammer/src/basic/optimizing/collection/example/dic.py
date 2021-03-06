#coding=utf-8
'''
字典（dict）
下列字典的平均情况基于以下假设：
1. 对象的散列函数足够撸棒（robust），不会发生冲突。
2. 字典的键是从所有可能的键的集合中随机选择的。

小窍门：只使用字符串作为字典的键。这么做虽然不会影响算法的时间复杂度，但会对常数项产生显著的影响，这决定了你的一段程序能多快跑完。

操作 平均情况 最坏情况 
复制[注2] O(n) O(n) 
取元素 O(1) O(n) 
更改元素[注1] O(1) O(n) 
删除元素 O(1) O(n) 
遍历[注2] O(n) O(n) 

'''
