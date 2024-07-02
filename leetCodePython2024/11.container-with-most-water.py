#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, current_max = 0, len(height)-1, 0

        while left < right:
            left_height, right_height = height[left], height[right]
            current_max = max((right-left)*min(left_height,
                              right_height), current_max)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return current_max

# @lc code=end
