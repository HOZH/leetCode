#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = [0 for i in range(len(nums))]

        ans[0] = nums[0]

        for i in range(1, len(nums)):
            temp = i-2
            if temp < 0:
                ans[i] = max(0+nums[i], ans[i-1])
            else:
                ans[i] = max(ans[temp]+nums[i], ans[i-1])

        return ans[-1]

# @lc code=end
