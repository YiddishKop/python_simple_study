"""
本节讲解如何获取目录地址及如何解决 import 失败的问题

如何获取本层及上层目录
--------------------

主要就是三个 os.path 函数:
- os.path.dirname(__file__)
- os.path.join()
- os.path.abspath()


如何解决 import 失败的问题
-----------------------

1. 首先每个包下应该有一个 __init__.py 其中定义了 __all__ 列表字段; 这样才能将其
用 from package import class or from package.class import method 的形式引入其下
的某个类 or 方法

2. 之后需要确定当前工程目录是否处在 sys.path 列表中, 如果不在则需要调用
sys.path.append(dir) 进行添加

3. 有时候需要获取上层目录 or 本层目录, 方法如下: 3.1 获取当前代码文件的本层目录
绝对地址: os.getcwd() 3.2 同上: os.path.dirname(__file__) 3.3 获取当前代码文件
的上层目录绝对地址: parent_name = os.path.join(os.path.dirname, os.pardir)
os.path.abspath(parent_name)

"""

import os
import sys

# 如下两个操作等价

os.getcwd()

os.path.dirname(__file__)

# 获取上层目录

current_dir_abspath = os.path.dirname(__file__)

parent_dir_name = os.path.join(current_dir_abspath, os.pardir)

parent_dir_abspath = os.path.abspath(parent_dir_name)


# 将目录添加到 sys.path 中, 如此方可 import

sys.path.append(current_proj_path)
