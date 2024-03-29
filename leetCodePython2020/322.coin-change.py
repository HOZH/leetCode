#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins = set(coins)
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            for j in coins:
                if i-j > 0:
                    dp[i] = min(dp[i], dp[i-j]+1)

        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange_temp(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0]*(amount+1)

        for i in coins:
            if i <= amount:
                dp[i] = 1

        for i in range(1, amount+1):
            if dp[i] == 0:
                temp_lis = []
                for j in coins:
                    if i-j > 0:
                        temp_lis.append(dp[i-j])

                dp[i] = min(temp_lis)+1 if len(temp_lis) > 0 else 99999

        return dp[-1] if dp[-1] < 99999 else -1

# @lc code=end
