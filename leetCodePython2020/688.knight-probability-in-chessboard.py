#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start

from collections import deque


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
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
