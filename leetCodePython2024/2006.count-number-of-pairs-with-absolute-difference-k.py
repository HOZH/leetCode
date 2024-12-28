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
        for i in nums:
            bag[i] += 1

        ans = 0
        keys = bag.keys()
        for i in keys:
            if i+k in keys:
                ans += bag[i] * bag[i+k]

        return ans


# @lc code=end
