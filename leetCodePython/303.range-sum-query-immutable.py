#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#


class NumArray:

    def __init__(self, nums: List[int]):

        self.ns = nums

        self.dp = [0]*len(self.ns)
        if len(nums):
            self.dp[0] = self.ns[0]

            for k in range(1, len(self.ns)):
                self.dp[k] = self.dp[k-1]+self.ns[k]

    def sumRange(self, i: int, j: int) -> int:

        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j]-self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
