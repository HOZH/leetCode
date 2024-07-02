#
# @lc app=leetcode id=2859 lang=python3
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if '{0:b}'.format(i).count('1') == k:
                ans += nums[i]

        return ans

# @lc code=end
