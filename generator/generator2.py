"""
本节讲解 generator --- 生成器函数, 用于产生一列东西的函数
生成器函数的定义必须满足如下规则:
1. 必须 yield 其实元素(起点)
2. 必须 yield 每次步进叠加后的结果(足记)
3. 一般情况下都包含一个 while 循环, 用于叠加步进, yield 叠加结果

生成器的使用:
1. 一般使用 next(生成器函数引用) 来产生下一个'脚印'
2. 可以使用 [i for i in 生成器] 来得到所有'足记'并转换成 list
"""

# 例一
# 我们经常使用的一个生成器是, 整数顺序生成器 range(start, stop, step)
for _ in range(0, 9, 1):
    print(_)

print(type(range(0, 9, 1)))



# 例一
# 我们可以模仿 range 定义自己的生成器
def yidrange(start, stop, step=1):
    current = start
    yield start
    while current < stop-1:
        current = current + step
        yield current

yidgen = yidrange(0, 9, 1)
print(next(yidgen))
print(next(yidgen))
print(next(yidgen))
print(next(yidgen))

yidgenlist = [i for i in yidrange(0, 9 ,1)]




# 例二
# 自己定义一个 fibonaci 生成器
# 1 1 2 3 5 8 13 21 ...
def fib_gen():
    a, b = 1, 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a+b
g = fib_gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# 例三
# 生成器对象放在 () 和 [] 中是完全两种意思
# - 放在 () 就是表示生成器
# - 放在 [] 表示把生成器转成列表, 类似 list(生成器对象)
squares_gen = (x*x for x in range(10))
squares_lst = [x*x for x in range(10)]



