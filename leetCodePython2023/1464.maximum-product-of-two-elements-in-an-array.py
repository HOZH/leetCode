#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = sorted(list(map(lambda x:x-1, nums)),reverse=True)
        return temp[0]*temp[1]
# @lc code=end

