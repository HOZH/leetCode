#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        length = len(nums)
        dp_sum = [[0 for _ in range(length+1)] for _ in range(length+1)]
        dp_min = [[float('inf') for _ in range(length+1)] for _ in range(length+1)]

        for i in range(1, length+1):
            for j in range(i, length+1):
                dp_sum[i][j] = dp_sum[i][j-1]+nums[j-1]
                dp_min[i][j] = min(dp_min[i][j-1], nums[j-1])

        result = float('-inf')

        for i in range(1,len(dp_sum)):
            for j in range(i,len(dp_sum[0])):
                    result = max(dp_sum[i][j]*dp_min[i][j], result)

        return result
 
# @lc 1code=end

