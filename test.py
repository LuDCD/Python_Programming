# from collections import defaultdict
#
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:  # 字典循环可以一下接两个
#     d[k].append(v)
#
# print(type(d))
#
# print(d)
#
# print(type(d['blue']) is list)
#
# print(dir(list))
#
# print(dir(tuple))
#
# print(dir(dict))
#
# help(list.__add__)

a = [{(0, 0)}, {(2, 3)}, {(3, 1)}]
a[1].update({(2,3)})
print(a)