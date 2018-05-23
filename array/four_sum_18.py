# coding: utf-8
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def four_sum(self, nums, target):
        nums.sort()
        res = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1
        return res


def main():
    s = Solution()
    print(s.four_sum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    main()

