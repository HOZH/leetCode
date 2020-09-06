#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start


class NumArray:

    def __init__(self, nums):

        length = len(nums)
        if length == 0:
            pass
        else:
            self.nums = nums

            self.one_d = [0] * length
            self.one_d[0] = nums[0]
            for i in range(1, length):
                self.one_d[i] = self.one_d[i - 1] + nums[i]

            # self.two_d = [[0 for i in range(length)] for j in range(length)]
            # self.two_d[0] = self.one_d[:]
            # # for i in range(1, length):
            # #     self.two_d[i][i] = nums[i]
            # # for i in range(1, length):
            # #     for j in range(length):
            # #         if i >= j:
            # #             continue
            # #
            # #         self.two_d[i][j] = self.two_d[0][j] - self.two_d[0][i - 1]
            #
            # print(self.two_d)

    def sumRange(self, i: int, j: int) -> int:

        if not self.one_d:
            return None
        else:
            if i == j:
                return self.nums[i]
            if i == 0:
                return self.one_d[j]
            else:
                return self.one_d[j]-self.one_d[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
