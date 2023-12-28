#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start

from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for key, val in c.items():
            if val == 1:
                ans += key
        return ans

# @lc code=end
