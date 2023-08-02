#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        bag = defaultdict(list)
        result = 0
        for i in range(len(nums)):
            for j in bag[nums[i]]:
                if i*j % k == 0:
                    print(i,j)
                    result += 1
            bag[nums[i]].append(i)

        return result

# @lc code=end
