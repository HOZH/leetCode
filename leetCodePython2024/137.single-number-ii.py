#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bag = defaultdict(int)
        for i in nums:
            bag[i] += 1

        for i in bag.keys():
            if bag[i] == 1:
                return i

# @lc code=end
