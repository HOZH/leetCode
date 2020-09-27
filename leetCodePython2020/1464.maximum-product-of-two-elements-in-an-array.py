#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start

# from itertools import combinations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # combs = list(combinations(nums, 2))
        # return max(list(map(lambda x: (x[0]-1)*(x[1]-1), combs)))
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

        # @lc code=end
