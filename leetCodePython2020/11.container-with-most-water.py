#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        result = -1

        while left < right:
            w = right-left
            if height[left] < height[right]:
                temp = height[left]*w
                left = left+1

            else:
                temp = height[right]*w
                right = right-1

            if result < temp:
                result = temp

        return result


# @lc code=end
