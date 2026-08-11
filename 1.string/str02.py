"""
1.str格式化：
- f-string              支持变量，表达式，格式化说明，调式语法{var=}
- str.format()          适合动态参数，字典解包
- string.Template       适合外部配置，只做简单变量替换
- 旧式%                 遗留语法

2.批量字符映射
- str.maketrans(a,b,c)
- str.translate()

3.编码转换
- str               逻辑文本
- bytes             原始二进制字节
- str.endcode()     str --> bytes
- b.decode()        bytes --> str

4.string标准库常量
- str.ascii_letters             大小写英文字母
- str.ascii_lowercase           小写字母a-z
- str.ascii_uppercase           大写字母A-Z
- str.digits                    数字
- str.punctuation               全部标点符号
- str.whitespace                空白字符：空格\t\n\r\v\f
"""
