#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        row_len, col_len = len(dungeon), len(dungeon[0])

        hp = [[float('inf')] * (col_len+1) for _ in range(row_len+1)]

        hp[row_len][col_len-1] = hp[row_len-1][col_len] = 1

        for x in range(col_len-1, -1, -1):
            for y in range(row_len-1, -1, -1):
                hp[y][x] = max(1, min(hp[y][x+1], hp[y+1][x])-dungeon[y][x])

        return hp[0][0]


# @lc code=end
