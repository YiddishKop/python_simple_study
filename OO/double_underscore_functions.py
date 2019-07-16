"""
本节讲解前后带双下划线的特殊函数的用法这些函数都是[通用函数]对于每个类都可用
只要你定义了相关的双下划线函数, 可以类比 java 中的 toString() 函数,只有
类中定义了这个函数, 才能参与 [string + 对象] 这种运算.

对于 python 而言:
- 类中定义 __len__, 可以直接使用 len(对象)
- 类中定义 __str__, 可以直接使用 str(对象) or print(对象), 否则打印对象的描述符, 类似 ShoppingList object at 0x7fa5dbbb4a58
- 类中定义 __del__, 会在该类的对象数目为零时调用
- 类中定义 __add__, 可以直接使用 对象+对象

还有其他的很多内置函数, 不一一举例:
__add__(self, other)
__sub__(self, other)
__mul__(self, other)
__floordiv__(self, other)
__mod__(self, other)
__divmod__(self, other)
__pow__(self, other)
__lshift__(self, other)
"""






class ShoppingList(object):

    def __init__(self, name, **items):
        self.items = items
        self.name = name

    def __len__(self):
        total_items = 0
        for _ in self.items:
            total_items += 1
        return total_items

    def __str__(self):
        return str(self.items)

    def __del__(self):
        print("{name}'s shoppingList is destroyed".format(name=self.name))
        
    def __add__(self, obj): # 注意这里两参数
        shop_dict = {}

        # [问题] : 融合两个 dict 累加相同的key的value
        #
        # 我的思路:
        # if common items:
        #     shop_dict.append(key=item, value=self.items.value + obj.items.value)
        # else:
        #     shop_dict.append(key=item, value=self.items.value or obj.item.value)
        # 
        # 作者的思路:
        # 先对融合后的 dict_total 用其中一个 dict 做一次初始化
        # 然后用第二个 dict 与被初始化之后的 dict_total 做 key 对比, 相同则相加, 不同则直接赋值
        
        for key,value in self.items.items():
            shop_dict[key] = value

        for key,value in obj.items.items():
            if key not in self.items.keys():
                shop_dict[key] = value
            else:
                shop_dict[key] += value

        return shop_dict
            
yid_shlist = ShoppingList("yid", apple=4, pear=5, banana=6)
chen_shlist = ShoppingList("chen", apple=5, pear=3, banana=6, pie= 12)

print(yid_shlist + chen_shlist)
print(len(yid_shlist))
print(yid_shlist)
