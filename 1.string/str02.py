"""
1.声明字符串
- '单引号'和"双引号"
- '''三单引号'''和三单双引号：保留换行和缩进，通常用于SQL和文档注释
"""
str0 = 'hello word'
str1 = "hello word"
str2 = '''
hello
word
'''
str3 = """
select * from user where PL='python'
"""
print(str0,str1,str2,str3)

"""
2.1字符串标准转义系列
- \'        单引号
- \"        双引号
- \\        反斜杆
- \n        换行LF
- \r        回车CR
- \t        水平Tab
- \v        垂直制表
- \f        换页
- \b        退格
- \0        NUL空字符
- \a        响铃
"""

"""
2.2数值转义
- 八进制            \xxx后面1-3位数字(0-7)
- 十六进制          \xHH,HH位两位十六进制(00-FF)
- 4位十六进制       \Uxxxx,(0-0xFFFF)
- 8位十六进制       \Uxxxxxxxx,全部Unicode
- \N{NAME}          按官方字符名称name显示字符串
"""

"""
2.3字节串bytes转义
- 字节串b'xxx'支持\' \" \t \r \n \v \a \b \f \000 \xhh
- 不支持\u \U \N{}
"""

'''
3.相关的内置函数
- repr(str)         返回字符串的源码形式，不可的字符转为转义系列
- ascii(str)        把非ASCII码转为\u的形式
- json.dumps()      JSON转义
'''

