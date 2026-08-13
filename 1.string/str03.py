"""
字符串切片
1.索引
- 索引为正表示从0开始，左往右
- 索引为负，表示从末尾开始，右往左
"""
strs = "ABC"
print(strs[1])      # B
print(strs[-1])     # C

"""
2.切片str[start:end:step]
- 三个参数可以省略，但冒号不要省略
- start         开始位置
- end           结束位置，但不包括在内，如果包括end了，下次从end开始切片就没数据了
- step          步长，默认是1,负数表示反向，步长为0会报错
- 切片越界不回报错，有多少切多少，但是索引取值会报错
"""
strs1 = "python"
print(strs1[:::])   # python，全切
print(strs1[:-1])   # pytho
print(strs[2:])     # thon
print(strs[::2])      # pto
print(strs[:-2])      # :pyth
print(strs[-4:])        # thon
print(strs[2:5])        # tho

"""
3.slice内置对象
- 把切片参数封装为对象，实现切片复用，字符串，列表，元组都可以使用
- slice[start:end:step]，参数填None代表对应位置省略
"""
strs2 = "pyhton"
sli = slice(2,5)    # 等于strs2[2,5]
print(strs2[sli])       # tho
sli2 = slice(None:None:-1)   # 反向
print(strs2[sli2])          # nohtyp

"""
4.注意
- 字符串不可变，所以切片不能赋值，但可以赋值个别的对象
- start,end,step反向冲突直接返回空字符串
- 切片返回新字符，原字符串不变
- step=0，要切片有不想切片，直接报错
- str[:]等价str，,但可变系列lsit[:]表示浅拷贝
"""
