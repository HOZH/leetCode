#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        piles = piles[len(piles)//3:]

        ans = 0
        for i in range(len(piles)):

            if i % 2 == 0:
                ans += piles[i]

        return ans


# @lc code=end
