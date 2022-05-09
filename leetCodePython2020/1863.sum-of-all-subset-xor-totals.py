#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(arr):
            length = len(arr)
            if not length:
                return 0
            if length == 1:
                return arr[0]

            return reduce(lambda x, y: x ^ y, arr)
        subset_arr = []

        for i in range(2**len(nums)):
            current = []

            for j in range(len(nums)):

                if i & 1 << j:
                    current.append(nums[j])
            subset_arr.append(current)

        return sum(map(lambda x: helper(x), subset_arr))


# @lc code=end
