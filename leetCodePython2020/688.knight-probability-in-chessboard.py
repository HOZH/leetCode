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

    def knightProbability_sec(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1 if (0 <= r < N and 0 <= c < N) else 0
        dp_prev = [[0 for _ in range(N)] for _ in range(N)]
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp_prev[r][c] = 1
        possibles = ((2, 1), (2, -1), (-2, 1), (-2, -1),
                     (1, 2), (1, -2), (-1, 2), (-1, -2))

        for _ in range(K):
            dp = [[0 for _ in range(N)] for _ in range(N)]

            for i in range(N):
                for j in range(N):
                    for add_i, add_j in possibles:
                        if N > i + add_i >= 0 and N > j + add_j >= 0:
                            dp[i + add_i][j + add_j] += dp_prev[i][j] / 8

            dp_prev = dp[:]
        return sum(sum(i) for i in dp)

    def knightProbability_temp(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1 if (0 <= r < N and 0 <= c < N) else 0
        dp_prev = [[0 for _ in range(N)] for _ in range(N)]
        dp = [[0 for _ in range(N)] for _ in range(N)]

        dp_prev[r][c] = 1

        possibles = ((2, 1), (2, -1), (-2, 1), (-2, -1),
                     (1, 2), (1, -2), (-1, 2), (-1, -2))

        queue = deque()

        count = 0

        queue.append((r, c))

        while count < K:

            dp = [[0 for _ in range(N)] for _ in range(N)]

            current_step_len = len(queue)

            temp_count = 0
            temp_set = set()

            while temp_count < current_step_len:

                current_prev = queue.popleft()
                chance = dp_prev[current_prev[0]][current_prev[1]] / 8

                for i, j in possibles:

                    i = current_prev[0] + i
                    j = current_prev[1] + j

                    if 0 <= i < N and 0 <= j < N:
                        dp[i][j] += chance
                        temp_set.add((i, j))

                temp_count += 1

            queue.extend(temp_set)
            dp_prev = dp[:]
            # for i in range(N):
            #     dp_prev[i] = dp[i][:]

            count += 1

        result = 0
        for i in dp:
            result += sum(i)
        return result

# @lc code=end
