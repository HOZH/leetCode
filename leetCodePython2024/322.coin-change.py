#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return amount
        dp = [float('inf')]*(amount+1)
        for i in range(1, len(dp)):
            if i in coins:
                dp[i] = 1
            else:
                for j in coins:
                    if i > j:
                        dp[i] = min(dp[i-j]+1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1

# @lc code=end
