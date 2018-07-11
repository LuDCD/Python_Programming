#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
描述
成绩分数百分制转为五级制的判断输出（建议使用异常处理try-except-else-finally）。

具体要求如下：

1）输入一个[0-100]内成绩数据，输出相应等级（A、B、C、D、E），
如输入为99，第一行输出为“输入成绩属于A级别。”；

2）当输入数据为其他字符或者超过范围，则输出“输入数据有误！”；

3）当成绩等级为A、B、C、D，则换行输出“祝贺你通过考试！”；

4）使用finally实现无论输入任何数据，均在最后输出“好好学习，天天向上！

@author: ZHOU Heng
"""


class Solution:

    def h2f(self):
        n = input()
        if n == "":
            print("好好学习，天天向上！")
        else:
            try:
                n = eval(n)
                if 0 <= n <= 100:
                    pass
            except:
                print("输入数据有误！")
            else:
                if 0 <= n <= 100:
                    if 0 <= n < 60:
                        s = "E"
                    elif 60 <= n < 70:
                        s = "D"
                    elif 70 <= n < 80:
                        s = "C"
                    elif 80 <= n < 90:
                        s = "B"
                    elif 90 <= n <= 100:
                        s = "A"
                    print("输入成绩属于{}级别。".format(s))
                    if s != "E":
                        print("祝贺你通过考试！")
                else:
                    print("输入数据有误！")
            finally:
                print("好好学习，天天向上！")


def main():
    sol = Solution()
    sol.h2f()


if __name__ == "__main__":
    main()
