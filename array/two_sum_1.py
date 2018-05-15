# coding: utf-8
from time import time

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def two_sum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        通过两个循环把nums的元素迭代一遍，找出和等于target的两个值。
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sum2(self, nums, target):
        '''
        以nums中的元素为key,角标作为value创建字典d
        循环迭代，找出target-nums[i]（即另一个数），是否存在于字典d的key中，同时要保证相对应的value不能是i

        '''
        range_num = range(len(nums))
        d = dict(zip(nums, range_num))
        # print(d)
        for i in range_num:
            complement = target - nums[i]
            if complement in d and d.get(complement) != i:
                return [i, d.get(complement)]

    def two_sum3(self, nums, target):
        '''
        思路同第二种方法类似，不同的是直接创建空的字典d
        每次迭代都对complement是否存在于d中判断，若没有则在d中创建d[nums[i]] = i
        这种做法，可以省去把nums作为key创建字典这一步，减少一次遍历，同时把字典的创建放在了判断的循环中

        '''
        range_num = range(len(nums))
        d = dict()
        for i in range_num:
            complement = target - nums[i]
            if complement in d:
                return [d.get(complement), i]
            d[nums[i]] = i


startTime = time()
print('startTime:{}'.format(startTime))
s = Solution()
nums = [2, 7, 11, 15]
target = 9
solution = s.two_sum3(nums, target)
endTime = time()
print('endTime:{}'.format(endTime))
print('solution:{}\nspend:{}'.format(solution, endTime-startTime))

