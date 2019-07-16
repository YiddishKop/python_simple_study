"""
本节讲解的是对象的序列化 serialization of python object
"""

# | Key Binding   | Description                                                                  |
# |---------------+------------------------------------------------------------------------------|
# | ~SPC m =~     | Reformat the buffer according to PEP8 using                                  |
# | ~SPC m d b~   | toggle a breakpoint using =wdb=, =ipdb=, =pudb= or =pdb=                     |
# | ~SPC m g a~   | go to assignment using =anaconda-mode-find-assignments= (~C-o~ to jump back) |
# | ~SPC m g b~   | jump back                                                                    |
# | ~SPC m g g~   | go to definition using =anaconda-mode-find-definitions= (~C-o~ to jump back) |
# | ~SPC m g u~   | navigate between usages with =anaconda-mode-find-references=                 |
# | ~SPC m h d~   | look for documentation using =helm-pydoc=                                    |
# | ~SPC m h h~   | quick documentation using anaconda                                           |
# | ~SPC m h H~   | open documentation in =firefox= using                                        |

# 一, 序列化字典和列表对象进文件中
import pickle

print(" 序列化---------------------")
# 准备序列话一个 dict 和一个 list
dict1 = {'a' : 100,
         'b' : 200,
         'c' : 300}

list1 = [400,
         500,
         600]

print(dict1)
print(list1)

# ========= ===============================================================
# Character Meaning
# --------- ---------------------------------------------------------------
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)
# ========= ===============================================================

# 打开一个文件操作句柄用于存储和展示序列化文件
output = open("save1.pkl", 'wb')


# pickle.dump(对象, 文件句柄, 协议)
# 调用 "泡菜" 的 "倾倒" 函数把字典和列表对象"倾倒"进文件中
pickle.dump(dict1, output, pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, output, pickle.HIGHEST_PROTOCOL)


# pickle.dumps(对象, 协议) 
# 如果只是想序列化并返回, 而不像存入文件中, 则 dump 中无需 'output' 参数
seri_result = pickle.dumps(dict1, pickle.HIGHEST_PROTOCOL)
print("the result is: {}".format(seri_result))


# 关闭文件操作句柄
output.close()

print(" 反序列化---------------------")

# 二, 反序列化文件中的二进制文件为字典和列表对象

## 获取一个文件的读句柄
inputFile = open("save1.pkl", 'rb')

## 通过"泡菜"对象的"加载"函数把文件中的对象加载出来
dict2 = pickle.load(inputFile)
list2 = pickle.load(inputFile)

inputFile.close()

print(dict2)
print(list2)

