#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from collections import defaultdict
from itertools import combinations


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        bag = defaultdict(list)

        for i in range(len(nums)):
            bag[nums[i]].append(i)

        res = 0

        for i in bag.values():
            for j, z in combinations(i, 2):
                res += 1 if (j*z) % k == 0 else 0

        return res


# @lc code=end
