#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 1

        ans = 0
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if current < 1:
                ans = max(1-current, ans)

        return max(ans, 1)

# @lc code=end
