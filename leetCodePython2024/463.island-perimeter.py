#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    # Subtract edges shared with other land cells
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2

        return result

    def islandPerimeter_temp(self, grid: List[List[int]]) -> int:
        self.ans = 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    visited = set([(i, j)])
                    ans = 0
                    while len(queue):
                        current_layer_size = len(queue)
                        while current_layer_size:
                            current_i, current_j = queue.popleft()
                            local_ans = 0
                            for i_offset, j_offset in moves:
                                new_i = current_i + i_offset
                                new_j = current_j + j_offset
                                if not (0 <= new_i < len(grid)) or not (0 <= new_j < len(grid[0])):
                                    local_ans += 1
                                elif (new_i, new_j) not in visited:
                                    if grid[new_i][new_j] == 1:
                                        queue.append((new_i, new_j))
                                        visited.add((new_i, new_j))
                                    else:
                                        local_ans += 1
                            current_layer_size -= 1
                            ans += local_ans
                    return ans


# @lc code=end
