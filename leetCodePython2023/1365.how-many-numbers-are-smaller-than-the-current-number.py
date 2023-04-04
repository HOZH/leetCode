#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        counter = defaultdict(int)
        dp = [0] * (max_num+1)
        ans = [0] * len(nums)

        for i in nums:
            counter[i] += 1
        for i in range(1, max_num+1):
            dp[i] = dp[i-1]+counter[i-1]
        for i in range(len(nums)):
            ans[i] = dp[nums[i]]

        return ans


# @lc code=end
