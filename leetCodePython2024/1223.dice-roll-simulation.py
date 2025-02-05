#
# @lc app=leetcode id=1223 lang=python3
#
# [1223] Dice Roll Simulation
#

# @lc code=start
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        # dp[i][j][k] count of sequence end with k consecutive j's at length i
        dp = [[[0 for _ in range(max(rollMax) + 1)]
               for _ in range(7)] for _ in range(n + 1)]
        kMod = 1e9 + 7
        for j in range(1, 7):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, 7):
                for l in range(1, 7):
                    if l != j:
                        dp[i][j][1] += sum(dp[i - 1][l]) % kMod
                    else:
                        # rollMax[j-1] -> 1-indexed, the rollMax count of value j
                        # [j-1]+1 -> 1-indexed
                        for k in range(1, rollMax[j - 1] + 1):
                            # k-1, 1-indexed, previous count on the same consecutive value
                            dp[i][j][k] += dp[i - 1][j][k - 1] % kMod

        temp = sum([(sum(i) % kMod) for i in dp[-1]])

        return int(temp % kMod)
        
# @lc code=end

