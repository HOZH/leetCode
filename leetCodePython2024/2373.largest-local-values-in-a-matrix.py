#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))

        def helper(i, j):
            local_max = float('-inf')
            for i_offset, j_offset in offsets:
                new_i, new_j = i+i_offset, j+j_offset
                if -1 < new_i < rows and -1 < new_j < cols:
                    local_max = max(local_max, grid[new_i][new_j])
            return local_max

        ans = []
        for i in range(1, rows-1):
            current_layer = []
            for j in range(1, cols-1):
                current_layer.append(helper(i, j))
            ans.append(current_layer)

        return ans


# @lc code=end
