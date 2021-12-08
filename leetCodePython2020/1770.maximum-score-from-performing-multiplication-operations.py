#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # dp -> ops to do
        # dp[op count][left side op count] , right op count = op count - lest side op count
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        dp[1][1] = multipliers[0] * nums[0]
        dp[1][0] = multipliers[0] * nums[-1]

        for i in range(2, m + 1):
            mult = multipliers[i - 1]
            for left in range(i + 1):
                right = i - left
                if left < 1:
                    dp[i][left] = mult * nums[-right] + dp[i - 1][left]
                elif right < 1:
                    dp[i][left] = mult * nums[left - 1] + dp[i - 1][left - 1]

                else:
                    dp[i][left] = max(mult * nums[left - 1] + dp[i - 1][left - 1],
                                      mult * nums[-right] + (dp[i - 1][left]))
        return max(dp[-1])

            

        
# @lc code=end

