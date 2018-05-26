# coding: utf-8
'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
'''
# 这道题的核心就是去重。可以用两个光标来指示，开始左右光标都在起始位置，每次迭代，右光标都加一，若左右光标处的值不同，
# 就把左光标加一，然后把新值赋给左光标，这样就完成了在原始的数组上去重，最后得到去重的数组。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur, pre = 0, 0
        while cur < len(nums):
            if nums[cur] != nums[pre]:
                pre += 1
                nums[pre] = nums[cur]
                cur += 1
            else:
                cur += 1
        return pre + 1