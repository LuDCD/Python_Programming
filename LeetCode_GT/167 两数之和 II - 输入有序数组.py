#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

@author: ZHOU Heng
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '超时！'
        '这样的数[0,...,0,2,3,9,...,9]  5'
        for i in range( len(numbers) ):
            b = target-numbers[i]
            if b in numbers[i+1:]:
                return [i+1, numbers[i+1:].index(b)+i+2]

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '超时！'
        '这样的数[0,...,0,2,3,9,...,9]  5'
        index1 = index2 = 0
        c = min( numbers )
        if target == 0 and c == 0:
            index1 = numbers.index(0) + 1
            index2 = numbers[index1:].index(0) + 2
        else:
            for i in range( c,target-c ):
                if i in numbers:
                    index1 = numbers.index(i) + 1
                    b = target - i
                    if b in numbers[index1:]:
                        if b != i:
                            index2 = numbers.index(b) + 1
                        else:
                            index2 = numbers[index1:].index(b) + index1 +1
                        break

        # 这种方法可能顺序不对
        return sorted( [index1, index2] )

    def twoSum3(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        别人更加优秀的代码！学习了！
        '''
        i = 0
        j = len(numbers) - 1
        while i < j:
            # while numbers[j] > target:
            #     j -= 1
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
        return



def test():
    # numbers = [2, 6, 3, 15];       target = 9
    # [2, 3]
    # numbers = [4, 4, 5, 1];     target = 8
    # [1, 2]
    # numbers = [2, 3, 4];      target = 6
    # [1, 3]
    # numbers = [-1,0];       target = -1
    # [1, 2]

    # numbers = [0,0,3,4];        target = 0
    # [1, 2]

    # numbers = [-3,3,4,90];      target = 0
    # [1, 2]

    numbers = [1,2,3,4,4,9,56,90];       target = 8
    # [4,5]
    sol = Solution()
    print( sol.twoSum2(numbers, target) )

if __name__ == "__main__":
    test()
'爆炸！终于成功了，错误率活活被他拉高了！！！'


