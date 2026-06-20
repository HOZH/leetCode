#
# @lc app=leetcode id=3512 lang=python3
#
# [3512] Minimum Operations to Make Array Sum Divisible by K
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if total < k:
            return total
        return total % k

# @lc code=end
