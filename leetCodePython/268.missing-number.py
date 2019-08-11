#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        temp_current = set(range(len(nums)+1))

        for i in nums:

            temp_current.remove(i)

        return temp_current.pop()
        

