#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#


class NumArray:

    def __init__(self, nums: List[int]):

        self.ns = nums

    def sumRange(self, i: int, j: int) -> int:

        return sum(self.ns[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
