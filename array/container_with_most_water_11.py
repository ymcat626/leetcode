# coding: utf-8
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

注意：你不能倾斜容器，n 至少是2。
'''


class Solution:
    # 首先分析题意，由坐标轴上两点，及其到x轴所做垂线构成的四边形，求其最大面积。
    # 面积 = （角标i - 角标n）* min（height[i], height[n]）
    # 第一种做法：从最左边开始，依次遍历每一种可能，比较大小，直到找到最大值。
    # 由于两次迭代，时间复杂度O(n*n)
    def max_area1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
                # if height[i] < height[j]:
                #     temp = (j - i) * height[i]
                # else:
                #     temp = (j - i) * height[j]
                # if max_area < temp:
                #     max_area = temp
        return max_area

    # 第二种做法：从两边开始判断，第一次求出最左边和最右边所构成的四边形面积，若l_height < r_height,
    # 说明最左边的点和其他所有的点形成的四边形都不可能比和最右边点形成的四边形面积大，故此最左边点可以抛弃。
    # 左边点角标加1
    # 这种算法优化了遍历，可以在一次遍历就完成目标。时间复杂度为O(n)
    def max_area2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left_num = 0
        right_num = len(height) - 1
        while left_num < right_num:
            max_area = max(max_area, min(height[left_num], height[right_num]) * (right_num - left_num))
            if height[left_num] < height[right_num]:
                left_num += 1
            else:
                right_num -= 1

        return max_area


def test():
    solution = Solution()
    print(solution.max_area2([1, 2]))


if __name__ == '__main__':
    test()
