#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
编写一个计算斐波那契数列的函数，采用递归方式，输出不超过n的所有斐波那契数列元素

调用上述函数，完成如下功能：

用户输入一个整数n，输出所有不超过n的斐波那契数列元素、输出数列的元素和及平均数，输出按照顺序，用英文逗号和空格分割

此题目为自动评阅，请严格按照要求规范输入和输出。

@author: ZHOU Heng
"""

class Solution:
    def fab(self):
        n = eval(input())
        fa = [0]
        while fa[-1] < n:
            if len(fa) == 1:
                fa.append(1)
            else:
                fa.append(fa[-1] + fa[-2])

        s = sum(fa)
        l = len(fa)
        avg = int(s/l)
        fa.append(s)
        fa.append(avg)

        for i in range(l+2):
            if i == 0:
                print(fa[i], end=',')
            elif i == l+2-1:
                print('', fa[i])
            else:
                print('', fa[i], end=',')


def main():
    sol = Solution()
    sol.fab()


if __name__ == "__main__":
    main()