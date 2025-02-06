#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        roots = dict()
        rank = dict()

        for i, j in edges:
            roots[i] = i
            roots[j] = j
            rank[i] = 1
            rank[j] = 1

        def find(a):
            # step is 1, a = a's root, root[a] = root of root of a
            # while roots[a] !=a:
            #     temp = roots[a]
            #     roots[a] = roots[roots[a]]
            #     a=temp
            # return a

            #####
            # 2023 revision
            if roots[a] != a:
                roots[a] = find(roots[a])

            return roots[a]

        for i, j in edges:

            pi, pj = find(i), find(j)

            if pi == pj:
                return [i, j]

            elif rank[roots[pi]] > rank[roots[pj]]:
                roots[pj] = pi
            elif rank[roots[pi]] < rank[roots[pj]]:
                roots[pi] = pj

            else:
                roots[pj] = roots[pi]
                rank[roots[pi]] += 1

        return []
# @lc code=end
