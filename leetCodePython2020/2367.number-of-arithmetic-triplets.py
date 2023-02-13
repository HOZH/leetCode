#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
from collections import defaultdict


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        first_count, second_count = defaultdict(int), defaultdict(int)
        bag = set(nums)

        for i in nums:
            if i-diff in bag:
                first_count[i] += 1
            if i-2*diff in bag:
                second_count[i] += 1

        result = 0

        for key in first_count.keys():
            result += first_count[key]*second_count[key]

        return result

# @lc code=end
