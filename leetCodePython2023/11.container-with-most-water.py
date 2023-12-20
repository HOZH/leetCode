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
            left_height, right_height = height[left], height[right]
            result = max(result, min(left_height, right_height)*(right-left))
            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return result


# @lc code=end
