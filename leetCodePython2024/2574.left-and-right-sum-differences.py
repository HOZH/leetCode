#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
from collections import deque


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = deque([0]), deque([0])
        length = len(nums)
        for i in range(1, length):
            left_sum.append(left_sum[-1]+nums[i-1])
        for i in range(length-1, 0, -1):
            right_sum.appendleft(right_sum[0]+nums[i])

        ans = []
        for i in range(length):
            ans.append(abs(right_sum[i]-left_sum[i]))

        return ans
# @lc code=end
