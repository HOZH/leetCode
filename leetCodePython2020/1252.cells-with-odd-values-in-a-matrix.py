#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_count, col_count = [0]*n, [0]*m
        for i in indices:
            row_count[i[0]] += 1
            col_count[i[1]] += 1

        result = 0
        for i in row_count:
            for j in col_count:
                if (i+j) % 2 != 0:
                    result += 1

        return result

# @lc code=end
