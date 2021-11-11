#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        container = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            ans += container[nums[i]-k]
            ans += container[nums[i]+k]

            container[nums[i]] += 1

        return ans

# @lc code=end
