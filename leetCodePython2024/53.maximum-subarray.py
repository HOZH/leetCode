#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current, ans = 0, float('-inf')

        for i in nums:
            current = max(current+i, i)
            ans = max(ans, current)

        return ans

# @lc code=end
