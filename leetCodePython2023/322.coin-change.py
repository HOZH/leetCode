#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf') for _ in range(amount+1)]

        for i in range(1, amount+1):
            for j in coins:
                temp = i-j
                if temp == 0:
                    dp[i] = 1
                elif temp > 0:
                    dp[i] = min(dp[i-j]+1, dp[i])
                    
        return dp[-1] if dp[-1] != float('inf') else -1

# @lc code=end
