#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        current_set = set()

        dup = -1

        for i in nums:

            if i in current_set:

                dup = i

            current_set.add(i)

        return [dup, set(range(1, len(nums)+1)).difference(current_set).pop()]
