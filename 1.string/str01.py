'''
1. string
- str字符串是不可变序列，所有修改操作不会修改原来字符，而是返回新字符对象
- 字符串支持索引，切片，遍历，内存一旦创建不能原地修改

2.string切片
- string[start:end:step],省略start从头开始，省略end到末尾，step步长，复数表示倒序

3.str内置方法（全部方法不会修改原字符串，返回新字符串）
- str.upper()           全部大写
- str.lower()           全部大写
- str.swapcase()        大小写互换
- str.capitalize()      首字母大写
- str.title()           每个单词首字母大写

4.去除空白字符串
- str.strip()               默认去除：空格\n,\t,\r
- str.lstrip()              去除左边
- str.rstrip()              去除右边

5.对齐填充
- str.center()              居中
- str.ljust()               左对齐
- str.rjust()               右对齐
- str.zfill()               补充0

6.查找
- str.find()                找不到返回-1，不抛出异常
- str.find(sub,start,end)  指定搜索范围查找
- str.index()               找不到抛出ValueError
- str.rfind()               从右侧反向查找
- str.rindex()              从右侧反向查找

7.判断开头结尾
- str.startwith()           以什么开头
- str.endwith()             以什么结尾

8.分割
- str.split(sep,maxsplit)       分割字符串，maxsplit设置最大分割数
- str.rsplit(sep,maxsplit)      反向分割字符串，maxsplit设置最大分割数
- partition(sep)                永远返回三元组(head,sep,tail)，找不到分隔符sep为空，不会报错
- rpartition(sep)               

9.拼接
- str.join(可到达对象)          把元组，列表里面的字符拼接

10.替换
- str.replace('old_str','new_str','index')    index表示只替换第index处

11.字符串判断方法（返回布尔值）
- str.isdigit()             是否全部是数字
- str.isalpha()             是否全部是字母
- str.isalnum()             是否是字母或数字
- str.isspace()             是否全部是空白字符
'''
