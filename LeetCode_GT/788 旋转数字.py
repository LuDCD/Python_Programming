#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
我们称一个数 X 为好数,
如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。
要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字，则这个数是有效的(0,1,2,5,6,8,9)。
0, 1, 和 8 被旋转后仍然是它们自己；
2 和 5 可以互相旋转成对方；6 和 9 同理，
除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

示例:
输入: 10
输出: 4
解释:
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。

注意:
N 的取值范围是 [1, 10000]。

@author: ZHOU Heng
"""


class Solution:
    def isRevolveNum(self, x):
        sx = str(x)     # 数字变成字符串
        flag = 1        # 默认数字是旋转数字
        #            0     1    2    3    4      5    6    7     8    9
        revolList = ['0', '1', '5', None, None, '2', '9', None, '8', '6']
        newNum = ''
        for k in sx:
            if k in '347':      # 有效的(0,1,2,5,6,8,9)
                flag = 0
                break
            else:
                newNum += revolList[ eval(k) ]

        # x 中不含'347'
        if flag == 1 and eval(newNum) == x:
            flag = 0

        return bool(flag)

    def isRevolveNum2(self, x):
        sx = str(x)     # 数字变成字符串
        flag = 0        # 默认数字不是旋转数字
        if set( '347' ) & set(sx) == set() and set('2569' ) & set(sx) != set():
            flag = 1

        #              0     1    2    3    4      5    6    7     8    9
        # revolList = ['0', '1', '5', None, None, '2', '9', None, '8', '6']

        return bool(flag)

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        numRot = 0
        for i in range(N+1):
            if self.isRevolveNum2(i):
                numRot += 1

        return numRot



def test():
    n = 9676
    sol = Solution()
    print( sol.rotatedDigits(n) )


if __name__ == "__main__":
    test()


