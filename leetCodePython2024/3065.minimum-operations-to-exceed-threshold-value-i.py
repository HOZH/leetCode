#
# @lc app=leetcode id=3065 lang=python3
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len(nums)-len(list(filter(lambda x: x >= k, nums)))

# @lc code=end
