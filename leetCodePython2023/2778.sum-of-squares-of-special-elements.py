#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements
#

# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            index = i+1
            if n % index == 0:
                result += nums[i]**2

        return result

# @lc code=end
