#coding=utf-8
'''
如果要对一个列表或者数组既要遍历索引又要遍历元素时，可以用enumerate
'''

a=[4,5,6,7,8,9]

for index,value in enumerate(a): 
    print index,value # 0 4
#     print a[index+1]
    
for index in enumerate(a): 
    print index#(3, 7)

    
'''
enumerate(sequence,start=0)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons)) 
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1)) 
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
'''

