#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定两个字符串, A 和 B。
A 的旋转操作就是将 A 最左边的字符移动到最右边。
例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false

注意：
A 和 B 长度不超过 100。

@author: ZHOU Heng
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        la = len( A )
        lb = len( B )

        if la != lb:    # A和B长度不等
            return False
        elif A == '':   # 长度相等，都为 空串''
            return True
        else:           # 长度相等，判断是否元素相同
            for k in B:
                if k not in A:
                    return False

        iba = [ a for a in range(len(A)) if A[a] == B[0] ]
        # 右上面的一系列操作，ln >= 1
        ln = len( iba )
        flag = 0        # 作为返回值，默认不是旋转支付串

        for ba in iba:
            if A[ba:] == B[:la-ba] and A[:ba] == B[la-ba:]:     #  两个串都对的上
                flag = 1
                break

        return bool(flag)


def test():
    # A = 'abcde';         B = 'cdeab'
    # A = 'abcde';           B = 'abced'
    # A = 'a';    B = 'a'
    # A = '';    B = ''
    # A= "ohbrwzxvxe";        B = "uornhegseo"
    # A = ''; B = 'a'
    A = "vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg";  B = "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"
    sol = Solution()
    print( sol.rotateString(A, B) )


if __name__ == "__main__":
    test()


