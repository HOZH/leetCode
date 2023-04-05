#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
from collections import defaultdict


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        bag = defaultdict(int)
        ans = 0

        for i in nums:
            if bag[i-diff] != 0:
                ans += bag[i-diff*2]
            bag[i] += 1

        return ans

# @lc code=end
