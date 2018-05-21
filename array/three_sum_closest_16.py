# coding: utf-8
'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
 Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
# 类似于three sum的问题，但是这里要求的是最接近于target的值，这样我们就必须对三个数的和与target进行比较，用diff表示。
# 每次比较之后，更新diff和closest的值。

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0] + nums[1] + nums[2]
        diff = abs(closest - target)
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                new_diff = abs(sum - target)
                if diff > new_diff:
                    diff = new_diff
                    closest = sum
                if sum < target:
                    l += 1
                else:
                    r -= 1

        return closest
