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

        # each vertex points to itself at beginning
        for i, j in edges:
            roots[i] = i
            roots[j] = j
            rank[i] = 1
            rank[j] = 1

        def find(a):

            x = a
            while roots[x] != x:
                roots[x] = roots[roots[x]]
                x = roots[x]

            return roots[x]

        for i, j in edges:

            pi, pj = find(i), find(j)

            if pi == pj:
                return [i, j]

            if rank[pi] > rank[pj]:

                roots[pj] = pi

            elif rank[pi] < rank[pj]:
                roots[pi] = pj

            else:

                roots[pj] = roots[pi]
                rank[pi] += 1

        return []


# @lc code=end
