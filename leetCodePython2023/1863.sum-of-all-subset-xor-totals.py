#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        length = len(nums)
        ans = 0
        for i in range(1 << length):
            temp = 0
            for j in range(length):
                if i & 1:
                    temp = temp ^ nums[j]
                i >>= 1
            ans += temp
        return ans
# @lc code=end
