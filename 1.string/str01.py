"""
一.字符串底层核心认知
1.不可变性(Immutable)
- 保证数据安全，运行哈希值缓存，极大提升查询速度
- 所有修改操作均返回新字符串，原字符串不改变
"""
strs = "hello word"
print(f"原str-->{id(strs)}")
print(f"strs-->{strs}")
strs = strs.upper()
print(f"修改后-->{id(strs)}")
print(f"strs-->{strs}")
"""
原str-->2430298736112
strs-->hello word
修改后-->2430298748528
strs-->HELLO WORD
"""

"""
2.字符串驻留(String Interning)
- python自动缓存[a-zA-Z0-9_]的字符串，相同的内容复用同一个对象
- 所以不要依赖is判断字符串相等，要用==
- is判断内存对象身份，==判断内容相等
"""
a = "hello_word"
b = "hello_word"
print(f"a is b -->{a is b}")
print(f"a-->{id(a)}")
print(f"b-->{id(b)}")
"""a is b -->True
a-->2186275342512
b-->2186275342512"""

"""
2.1全局字符串驻留inter（全局池）
- 条件：字符串只能是[a-zA-Z0-9_]，不能有空格，下划线，标点
- 作用：跨函数，跨行，跨模块共享同一个对象
- 带空格和！的字符串不会进入全局池
>>> c = "hello word!"
>>> d = "hello word!"
>>> c is d        # 在交互环境下，每一行但是独立的代码
False
>>> id(c)
2591187849712
>>> id(d)
2591187848880
"""

"""
2.2代码对象内部常量去重(Constantfolding,字节码编译器优化)
- 同一个.py文件，同一个函数里面，数值量相同的两个变量属于同一个字节码对象
- 编译的时候，python会扫描全部字面量，同一代码块内，内容完全一样的字面常量
  直接合并成一个对象，不管有没有空格，感叹号
"""
c = "hello word!"
d = "hello word!"
print(f"c is d -->{c is d}")  # 按理说应该是False，但是编译器自动去重了
print(f"c-->{id(c)}")
print(f"d-->{id(d)}")
""""
c is d -->True
c-->2186275342768
d-->2186275342768"""

"""
2.3手动强制加入全局驻留池
"""
import sys
str1 = 'hello word!'
str2 = 'hello word!'
print(str1 is str2)   # 脚本内True，在交互环境下False
str3 = sys.intern("hello word!")
str4 = sys.intern("hello word!")
print(str3 is str4)    # 都为True

"""
二.哈希缓存
1.1哈希值hash(s)
- 调用内置函数hash(str)，就会得到一个整数，这个整数就是字符串的哈希值
- 作用：dict的key查找，set集合去重
"""
# 把任意长度的数据，通过哈希算法，算出一段固定长度的乱码字符串
str5 = "myun"
print(f"str5哈希值-->{hash(str5)}")     # str5哈希值-->2837929074394432124

"""
1.2哈希算法特性
- 输出长度固定
  - MD5:输出32位
  - SHA-1:40位
  - SHA256:64位

- 雪崩效应
  - 原始数据只要修改一个地方，算出来的哈希值完全不一样，几乎没有相似的地方

- 单向不可逆
  -只能从原始数据到哈希值，不能拿哈希值反推原数据

- 确定性
  - 同样的数据，用同一个哈希算法，无论算多少次，得到的哈希结果完全一模一样
"""

"""
2.哈希缓存机制
- str对象结构体里面有一个内部字段ob_hash，用来保存已经计算过的哈希值
  a.字符串对象创建的时候，ob_hash = -1，表示哈希还没有计算
  b.第一次调用hash(str),=，计算哈希值，把哈希值存入对象内部ob_hash，缓存起来
  c.之后再调用hash(str),不需要在重新计算哈希值，直接读取计算好的on_hash
"""
str6 = "python"
print(f"first-->{hash(str6)}")
print(f"second-->{hash(str6)}")
print(f"third-->{hash(str6)}")
# first-->4714252391874340451
# second-->4714252391874340451
# third-->4714252391874340451

