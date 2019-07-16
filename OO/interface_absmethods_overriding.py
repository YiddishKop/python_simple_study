"""
python 想使用接口或是抽象类, 要比 java 多做一些工作,
需要引入 abc 包中的 ABCMeta 函数和 abstractmethod 标签
"""


# [知识点]
# 想使用接口/抽象类等定义,必须引入这个包
from abc import ABCMeta, abstractmethod

# Interface
class Shape(object):

    # [知识点]
    # 当你希望把这个类声明为接口or抽象类,并且其中的两个函数必须被
    # 子类实现的时候,就必须在该类中
    # 1. 声明 __metaclass__ 字段为 ABCMeta
    # 2. 抽象函数头添加 @abstractmethod 标签

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self):pass


s=Shape()       # tutorial 中说这里会报错,但是却没有
print(s.area()) # None


# implement interface Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # [知识点]
        # __init__ 函数相当于构造函数, 我们一般希望当我们构建
        # 子类对象的时候, 也会构造父类对象, 所以我们如此书写:
        # 必须在每一个 __init__ 函数定义中调用 super().__init__()
        # 并且将子类类名作为参数传递其中
        super(Rectangle, self).__init__()

    def area(self):
        print("using rectangle area method")
        return self.width * self.height

    def perimeter(self):
        print("using rectangle perimiter method")
        return 2*(self.width + self.height)

rect = Rectangle(5, 7)  # 创建一个 Rectangle 对象 
print(rect)
print(rect.area())      # 35
print(rect.perimeter()) # 24


# extends class Rectangle
class Square(Rectangle):

    def __init__(self, side_length):
        self.side_length = side_length
        super(Square, self).__init__(side_length, side_length)

    def area(self):
        print("using square area method")
        return self.side_length ** 2

    def perimeter(self):
        print("using square perimeter method")
        return 4 * self.side_length


square = Square(12)
print(square)
print("side lenth = {length} , and square area = {area}".format(length = square.side_length, area = square.area()))
print("side lenth = {length} , and square perimiter = {perimeter}".format(length = square.side_length, perimeter = square.perimeter()))
