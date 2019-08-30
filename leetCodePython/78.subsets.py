#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


class Solution:
    def subsets(self, nums):
        result = [[]]
        for elem in nums:
            result.extend([x + [elem] for x in result])
        return result
