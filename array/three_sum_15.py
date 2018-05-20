# coding: utf-8
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 思路：首先暴力解析确实可行，但是时间复杂度太高。所以，可以把其中一个数拿出来，剩余的两个数之和是确认的，
        # 这样问题就回到两个数求和的问题。
        # 1.首先对nums进行排序。
        # 2.判断我们所选的数字是否大于零，大于零在这里是没有意义的。因为大于零的有序数组，三个数和是不可能为零的。
        # 3.排除重复的数字，如果nums[i]==nums[i-1]，continue
        # 4.标记lo和hi，即从两头开始进行遍历求和
        # 5.最后判断成功时，lo和hi要各自进行加1的处理，并且过滤掉重复的元素。
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s > 0:
                    hi -= 1
                elif s < 0:
                    lo += 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return res


def main():
    s = Solution()
    print(s.three_sum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()
