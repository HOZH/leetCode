#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def min_prev_path_sum(i, j):
            prev_layer_len = len(triangle[i])
            local_sums = []
            if j-1 >= 0:
                local_sums.append(triangle[i][j-1])
            if -1 < j < prev_layer_len:
                local_sums.append(triangle[i][j])
            return min(local_sums)

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min_prev_path_sum(i-1, j)

        return min(triangle[-1])


# @lc code=end
