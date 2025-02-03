#
# @lc app=leetcode id=3427 lang=python3
#
# [3427] Sum of Variable Length Subarrays
#

# @lc code=start
from functools import lru_cache


class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        @lru_cache(None)
        def get_sub_array_sum(start, end):
            if start == end:
                return nums[start]
            return get_sub_array_sum(start, end-1) + nums[end]

        ans = 0
        for i in range(len(nums)):
            ans += get_sub_array_sum(max(0, i-nums[i]), i)

        return ans

# @lc code=end
