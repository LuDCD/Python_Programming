#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
给定一个排序数组，你需要在【原地】删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

@author: ZHOU Heng
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 这个超时间限制了
        l = len( nums )
        for i in range( l ):
            val = nums[i]
            n = nums.count( val )
            if n != 1:
                for i in range( n-1 ):
                    j = nums.index( val )       # 找到 val 所在位置的序号
                    nums[j] = None              # 把它置为 None

        # 删除所有None
        n = nums.count( None )
        for i in range( n ):
            j = nums.index( None )       # 找到 元素None 所在位置的序号
            del nums[j]

        return len( nums )

    def removeDuplicatesSet(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        # 用集合
        # 也超时了！
        aSet = set( nums )
        for k in aSet:
            while nums.count(k) != 1:
                i = nums.index( k )
                del nums[i]

        return len( nums )

    def removeDuplicates3(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        # 排序法
        # 超时！
        nums.sort()
        l = len( nums )

        for i in range( l-1 ):
            if nums[i+1] == nums[i]:
                nums[i] = None

        n = nums.count(None)
        for i in range( n ):
            j = nums.index(None)
            del nums[j]

        return len( nums )

    def removeDuplicatesSpace(self, nums):
        # 终于过了！
        # 多用了一个 nums 大小的空间
        l = len( nums )
        if nums == []:
            return l

        nums1 = nums.copy()     # 开辟新的内存，来存储
        # nums1 = nums          # 这不行，因为这还是一块内存，知识两个指针。
        nums.clear()

        nums1.sort()
        for i in range( l-1 ):
            t = nums1[i]
            if nums1[i+1] != t:     # 如果后一个不等于前一个，则说明他是相同元素的最后一个
                nums.append( t )
        # 无论nums[-2]的元素是什么，最后一个都要加上。
        # 因为如果[-2]和[-1]不同，自然是要加上；
        # 如果[-2]和[-1]相同，[-2]没加添进去，[-1]必须加上。
        nums.append( nums1[-1] )

        return len( nums )

def test():
    # nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    # nums = [1,1]
    # nums = [1]
    nums = []
    print( nums )
    sol = Solution()
    # print( sol.removeDuplicates(nums) )
    # print( sol.removeDuplicates2(nums) )
    # print( sol.removeDuplicates3(nums) )
    print( sol.removeDuplicatesSpace(nums) )
    print( nums )


if __name__ == "__main__":
    test()


