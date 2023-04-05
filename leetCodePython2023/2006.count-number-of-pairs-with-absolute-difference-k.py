#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        bag = defaultdict(int)
        ans = 0
        for i in nums:
            bag[i] += 1
            ans += bag[i+k]
            ans += bag[i-k]

        return ans


# @lc code=end
