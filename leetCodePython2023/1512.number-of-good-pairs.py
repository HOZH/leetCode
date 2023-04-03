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
        bag = defaultdict(int)
        for i in nums:
            ans += bag[i]
            bag[i] += 1

        return ans


# @lc code=end
