#!/usr/bin/python
# -*- coding:utf8 -*-


# range(stop) -> range object
# range(start, stop[, step]) -> range object

# range(a,b)    表示 [a,b)
for count in range(1,10,1):
    if count%2 != 0:
        print(count)   #嘎嘎嘎
        continue    #控制的是循环
    print(count+10)

print()
nums = [0,2,4,6,8,10]
print('len(nums)=%d' % len(nums) )
for i in range(0,len(nums)):
    print( i )
    if nums[i] % 2 == 0:
        del nums[i]
'''
for i in range(10):
    if nums[i] % 2 == 0:
        list1 = list( range(len(nums)) )
        del nums[i]
        print(list1)
'''