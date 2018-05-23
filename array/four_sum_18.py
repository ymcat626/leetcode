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
        res = []
        for i in range(len(nums) - 3):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or j > i + 1 and nums[j] != nums[j - 1]:
                        l = j + 1
                        r = len(nums) - 1
                        while l < r:
                            sum = nums[i] + nums[j] + nums[l] + nums[r]
                            if sum == target:
                                res.append((nums[i], nums[j], nums[l], nums[r]))
                                r -= 1
                                l += 1
                                while l < r and nums[l] == nums[l - 1]:
                                    l += 1
                                while r > l and nums[r] == nums[r + 1]:
                                    r -= 1

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
