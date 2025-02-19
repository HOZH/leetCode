#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = [[False for _ in range(len(grid[0]))]
                   for _ in range(len(grid))]
        ans = 0
        next_positions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not checked[i][j]:
                    ans += 1
                    queue = deque([[i, j]])
                    while len(queue):
                        current_layer_len = len(queue)
                        while current_layer_len:
                            current_i, current_j = queue.popleft()
                            if not checked[current_i][current_j]:
                                checked[current_i][current_j] = True
                            else:
                                current_layer_len -= 1
                                continue
                            for next_i, next_j in next_positions:
                                new_i, new_j = next_i + current_i, next_j + current_j
                                if (
                                    -1 < (new_i) < len(grid)
                                    and -1 < new_j < len(grid[0])
                                    and not checked[new_i][new_j]
                                    and grid[new_i][new_j] == "1"
                                ):
                                    queue.append([new_i, new_j])

                            current_layer_len -= 1

        return ans

# @lc code=end
