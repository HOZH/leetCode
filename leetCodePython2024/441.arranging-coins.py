#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)(sqrt(2 * n + 0.25) - 0.5)

        
# @lc code=end

