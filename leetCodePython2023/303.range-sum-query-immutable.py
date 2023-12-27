#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]*len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1]+nums[i]

        self.sums = [0]+self.sums

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
