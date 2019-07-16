"""
本节介绍装饰器函数, 装饰器函数必须:
1. 接受函数作为参数;
2. 定义内置函数(inner-function), 用于接受被装饰函数的参数;
3. 返回内置函数

                         @decored_fun
                         def decored_fun(x,y):pass
                             ----------- ---     
                                |         | 
               +----------------+         | 
               |                          | 
               |                          | 
               v                          | 
def decor_fun(fun):                       | 
    def inner(*args):                     | 
        pass     ^------------------------+ 
    return inner

"""

def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
def reverse_string(string):
    return str(reversed(string))

print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string("A man, a plan Panama!"))
