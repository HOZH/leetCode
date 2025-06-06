#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# from collections import defaultdict


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         bag = defaultdict(int)
#         for i in nums:
#             bag[i] += 1

#         for i, j in bag.items():
#             if j == 1:
#                 return i


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


# @lc code=end
