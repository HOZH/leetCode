#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        a = tuple(filter(lambda x: x != val, nums))

        for i in range(len(nums)):

            nums[i] = None

        nums.extend(a)

        nums.sort(key=lambda x: x == None)

        return len(a)
