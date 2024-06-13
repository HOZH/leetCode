#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        num_bag = defaultdict(int)
        for i in range(len(nums)):
            ans += num_bag[nums[i]]
            num_bag[nums[i]] += 1

        return ans


# @lc code=end
