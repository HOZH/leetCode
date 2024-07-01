#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counts = defaultdict(int)
        ans = 0
        for i in nums:
            for j in counts.keys():
                if j < target-i:
                    ans += counts[j]
            counts[i] += 1

        return ans


# @lc code=end
