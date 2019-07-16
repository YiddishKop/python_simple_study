"""
本节介绍关于 np.outer 运算函数的意义

np.outer(arr1, arr2) ---> arr

该函数是对两个向量进行 outer product 运算, outer product 不同于 inner product,
他相当于先把两个向量看成两个元素列表, 对这两个列表进行 catesian product 获得笛卡尔积集
之后, 每一对进行乘法运算

Given two vectors,

``a = [a0, a1, ..., aM]``

and

``b = [b0, b1, ..., bN]``,

the outer product is::

  [[a0*b0  a0*b1 ... a0*bN ]
   [a1*b0    .
   [ ...          .
   [aM*b0            aM*bN ]]

"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([5,0,1])

arr_outer = np.outer(arr1, arr2)

print(arr_outer)
