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
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        range_num = range(len(nums))
        d = dict(zip(nums, range_num))
        # print(d)
        for i in range_num:
            complement = target - nums[i]
            if complement in d and d.get(complement) != i:
                return [i, d.get(complement)]

    def twoSum3(self, nums, target):
        range_num = range(len(nums))
        d = dict()
        for i in range_num:
            complement = target - nums[i]
            if complement in d:
                return [d.get(complement), i]
            d[nums[i]] = i


startTime = time()
print(startTime)
s = Solution()
nums = [2, 7, 11, 15]
target = 9
solution = s.twoSum3(nums, target)
endTime = time()
print(endTime)
print('solution:{}\nspend:{}'.format(solution, endTime-startTime))

