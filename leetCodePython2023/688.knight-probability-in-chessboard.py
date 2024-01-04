#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
from collections import deque


class Solution:
    # Define dp(r, c, k) as the probability that the knight on(r, c) remains on the board after k moves. We’ll get the recursion below: dp(r, c, k) = sum_for_allowed_moves(dp(r_new, c_new, k - 1)) / 8
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        possibles = ((2, 1), (2, -1), (-2, 1), (-2, -1),
                     (1, 2), (1, -2), (-1, 2), (-1, -2))

        @lru_cache(None)
        def helper(r, c, k):
            if not N > r >= 0 or not N > c >= 0:
                return 0
            if k <= 0:
                return 1
            res = 0
            for a, b in possibles:
                res += helper(r+a, c+b, k-1)
            return res/8
        return helper(r, c, K)
# @lc code=end

