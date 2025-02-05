#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_to_index = [0]
        for i in range(len(nums)):
            self.sum_to_index.append(self.sum_to_index[-1]+nums[i])
        self.sum_to_index = self.sum_to_index[1:]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_to_index[right]
        return self.sum_to_index[right]-self.sum_to_index[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
