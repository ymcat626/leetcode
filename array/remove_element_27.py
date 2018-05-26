# coding: utg-8
'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''
# 目的是去除数组中的某个元素，思路也很简单，在一个for循环中，如果nums[i]不等于target，我们让nums[new_tail] = nums[i]即可。
# 这样，数组中等于target的值全没有保存。

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0

        new_tail = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_tail] = nums[i]
                new_tail += 1

        return new_tail