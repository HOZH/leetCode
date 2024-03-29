#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # case amount is in coins
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[-1]


# @lc code=end
