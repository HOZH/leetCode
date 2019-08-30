#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = set(nums)

        length = len(a)

        if length == 0:

            return None

        if length == 1:

            return a.pop()

        if length == 2:

            return max(a)

        if length == 3:

            return min(nums)

        else:

            a.remove(max(a))
            a.remove(max(a))

            return max(a)
