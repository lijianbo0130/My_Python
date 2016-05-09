#coding=utf-8
'''


遇到问题: TypeError: %d format: a number is required, not str
解决办法: 传给sql的变量写对格式就行了. sql里不需要对对应的变量写%d,只写%s就可以了
list_insert=[(u"武汉","1")]
"1"可以当做num 插入


遇到问题: (1146, "Table 'database.'table_name'' doesn't exist")
解决办法: 不用cursur.execute(sql,param)方式,改成拼串方式写. str写成 column = '%s' , 
int写成 column = %s. 所有的int不需要加单引号. str需要单引号


遇到问题 ProgrammingError: (1064, "You have an error in your SQL syntax; 
check the manual that corresponds to your MySQL server version for
the right syntax to use near 'key,value) 
values\n('\xe6\xad\xa6\xe6\xb1\x89','1')' at line 1")
不要用key 或者value作为字段名

遇到问题 AttributeError: 'Cursor' object has no attribute 'exacute'
拼写错误 execute

问题   有问题最好重启
'''