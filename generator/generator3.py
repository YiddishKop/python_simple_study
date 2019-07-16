"""
本节主要讲解 python 中自带的一个生成器包 itertools
里面有非常多有用的生成器函数


itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算。

| Iterator                                 | Arguments                   | Results                                                       | Example                                                   |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| infinite iterator                        |                             |                                                               |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| count()                                  | start, [step]               | start, start+step, start+2*step, ...                          | count(10) --> 10 11 12 13 14 ...                          |
| cycle()                                  | p                           | p0, p1, ... plast, p0, p1, ...                                | cycle('ABCD') --> A B C D A B C D ...                     |
| repeat()                                 | elem [,n]                   | elem, elem, elem, ... endlessly or up to n times              | repeat(10, 3) --> 10 10 10                                |
|                                          |                             |                                                               |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| shortest sequence                        |                             |                                                               |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| chain()                                  | p, q, ...                   | p0, p1, ... plast, q0, q1, ...                                | chain('ABC', 'DEF') --> A B C D E F                       |
| compress()                               | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), ...                           | compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F             |
| dropwhile()                              | pred, seq                   | seq[n], seq[n+1], starting when pred fails                    | dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1           |
| takewhile()                              | pred, seq                   | seq[0], seq[1], until pred fails                              | takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4             |
| groupby()                                | iterable[, keyfunc]         | sub-iterators grouped by value of keyfunc(v)                  |                                                           |
| filter()                                 | pred, seq                   | elements of seq where pred(elem) is true                      | ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9           |
| filterfalse()                            | pred, seq                   | elements of seq where pred(elem) is false                     | ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8      |
| slice()                                  | seq, [start,] stop [, step] | elements from seq[start:stop:step]                            | islice('ABCDEFG', 2, None) --> C D E F G                  |
| map()                                    | func, p, q, ...             | func(p0, q0), func(p1, q1), ...                               | imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000                |
| starmap()                                | func, seq                   | func(*seq[0]), func(*seq[1]), ...                             | starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000        |
| tee()                                    | it, n                       | it1, it2, ... itn splits one iterator into n                  |                                                           |
| zip()                                    | p, q, ...                   | (p[0], q[0]), (p[1], q[1]), ...                               | izip('ABCD', 'xy') --> Ax By                              |
| zip_longest()                            | p, q, ...                   | (p[0], q[0]), (p[1], q[1]), ...                               | izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D- |
|                                          |                             |                                                               |                                                           |
|                                          |                             |                                                               |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| Combinatoric generators:                 |                             |                                                               |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|
| product()                                | p, q, ... [repeat=1]        | cartesian product, equivalent to a nested for-loop            |                                                           |
| permutations()                           | p[, r]                      | r-length tuples, all possible orderings, no repeated elements |                                                           |
| combinations()                           | p, r                        | r-length tuples, in sorted order, no repeated elements        |                                                           |
| combinations_with_replacement()          | p, r                        | r-length tuples, in sorted order, with repeated elements      |                                                           |
| product('ABCD', repeat=2)                |                             | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD               |                                                           |
| permutations('ABCD', 2)                  |                             | AB AC AD BA BC BD CA CB CD DA DB DC                           |                                                           |
| combinations('ABCD', 2)                  |                             | AB AC AD BC BD CD                                             |                                                           |
| combinations_with_replacement('ABCD', 2) |                             | AA AB AC AD BB BC BD CC CD DD                                 |                                                           |
|------------------------------------------+-----------------------------+---------------------------------------------------------------+-----------------------------------------------------------|

"""

from itertools import *


# ---------- 有限生成器 ---------- 
# 例一
# 链接器: 接收多个可遍历对象, 从一个可遍历对象(iterable)遍历, 然后下一个, 然后下一个,...,直到遍历完所有对象
# chain(*iterables) --> chain object

for i in chain('abc', '123'):
    print(i)
    
# 例二
# 掩模器: 接收两个可遍历对象, 第二个作为第一个的掩模---从中过滤掉对应位置为 0 or False 的元素, 只显示对应位置为 1 or True 的元素.
# 掩模长度不够的位置, 自动设置为 0 or False
# compress(data, selectors) --> iterator over selected data

for i in compress('abcdefg', [1,1,1,True,False,True]):
    print(i)

# 例三
# 丢弃器: 接收两个参数, 第一个为 functor 返回 boolean, 第二个为可遍历对象, 干掉符合条件的元素
# dropwhile(predicate, iterable) --> dropwhile object

for i in dropwhile(lambda x: x<=1, [1,2,3,4,1,2,3,4]):
    print(i)

# 例四
# 分组器: 接收两个参数, 第一个为可遍历对象, 第二个为 functor, 把可遍历对象中的每个元素投入 functor 做运算, 并把产生相同结果的元素分成一组
# 比较蛋疼的是, groupby 返回一个两层的 iterator, 外面是 iterator or items, 每个 item 是一个 tuple, tuple 的第二个元素是 iterator
# of value
# groupby(iterable, key=None) --> iterator of tuple(key, value_iterator) 

keys = []
values = []
for i,j in groupby([1,2,3,4,5], lambda x:x%2):
    keys.append(i)
    values.append(list(j))

print(keys)
print(values)


# 例五
# 映射器
# map(functor, iterator)    
for i in map(lambda x:x+1, [1,2,3,4,5]):
    print(i)

    
# 例五
# 变种映射器: 他与 map 最大的不同就是, 第二个参数是一个双层遍历对象, 内层的遍历对象是作为 functor 的参数列表传入
# starmap(functor, iterator of iterator)    
for i in starmap(lambda x:x+1, [[1],[2],[3],[4],[5]]):
    print(i)

    
# 例六
# 过滤器
# filter(functor, iterator)    
for i in filter(lambda x:x>0, [1, -1, 2,3,0]):
    print(i)

    
# 例五
# 组合器
# zip(iterator, iterator) --> iterator
for i in zip('abc', [1,2,3]):
    print(i)


# ---------- 无限生成器 ---------- 
# [注] 无限生成器会无限循环产生元素, 只能通过 Ctrl+c 退出, 故而注释掉
# 例一
# 数数器
# for i in count(1, 2):
#     print(i)
    
# print([i for i in count(1, 2)])

# 例二
# 循环器
# for i in cycle("ABC"):
#     print(i)
    
# print([i for i in cycle(1, 2)])

# 例三
# 重复器
for i in repeat('abc', 4):
    print(i)

print([i for i in repeat('abc', 4)])


# ---------- 组合生成器 ---------- 
# 例一
# 排列
for i in permutations('abc', 2):
    print(i)

print([i for i in permutations('abc', 2)])

# 例二
# 组合
for i in combinations('abc', 2):
    print(i)

print([i for i in combinations('abc', 2)])

# 例三
# 带放回的组合(可出现重复元素)
for i in combinations_with_replacement('abc', 2):
    print(i)

print([i for i in combinations_with_replacement('abc', 2)])

# 例四
# 笛卡尔积集
for i in product('abc', '123'):
    print(i)

print([i for i in product('abc', '123')])


