#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        array1 = sorted(nums)
        product = (array1[len(array1)-1] * array1[len(array1)-2]) - (array1[0] * array1[1]) 
        return product
# @lc code=end

