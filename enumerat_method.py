"""本节介绍 enumerat() 函数的使用:

1. enumerate在字典上是枚举、列举的意思

2. 对于一个可遍历的对象（iterable）如列表、字符串, enumerate 能将其组成一个带索
引的序列，利用它可以同时获得索引和值

"""

test_str = 'abcdefg'

# 可以看到一个可遍历对象通过 enumerate 后获得的是一个 enumerate 对象
print(type(enumerate(test_str)))


# 展示如何通过 enumerate 同时获取位置索引和值
dict = {}
for index, item in enumerate(test_str):
    dict[index] = item

print(dict)
