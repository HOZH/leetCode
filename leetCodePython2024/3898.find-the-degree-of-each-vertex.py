#
# @lc app=leetcode id=3898 lang=python3
#
# [3898] Find the Degree of Each Vertex
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # vertice_degrees = defaultdict(int)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         has_out_degree_to_j = matrix[i][j] == 1
        #         if has_out_degree_to_j:
        #             vertice_degrees[j] += 1

        # ans = [0] * len(matrix)
        # # for key, value in vertice_degrees.items():
        # #     ans[key]=value
        # ans = [vertice_degrees.get(i, 0) for i in range(len(matrix))]

        # return ans
        return list(map(lambda x: sum(x), matrix))


# @lc code=end
