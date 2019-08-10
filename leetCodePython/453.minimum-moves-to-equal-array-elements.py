#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#


class Solution:
    def minMoves(self, nums: List[int]) -> int:

        count=0
        
        lower = min(nums)

        for i in nums: count+=i-lower

        return count

