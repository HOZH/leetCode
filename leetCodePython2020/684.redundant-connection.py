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
            #####
        



            while roots[a] != a:
                # step is 2, previous method has step = 1, a = root of a's root
                # regradless what step is, the answer stays constant once
                # roots[a] == a, so this is correct and faster
                # root[a] != a
                # so a's root = root[ a's root -> root[a]] 
                temp = roots[roots[a]]
                roots[a] = temp # step is 1
                a = temp # step is 2

                # short but it's the same

                # roots[a] = roots[roots[a]]
                # a = roots[a]
            return a

        for i, j in edges:

            pi, pj = find(i), find(j)

            if pi == pj:
                return [i, j]

            elif rank[pi] > rank[pj]:
                roots[pj] = pi
            elif rank[pi] < rank[pj]:
                roots[pi] = pj

            else:
                roots[pj] = roots[pi]
                rank[pi] += 1

        return []


# @lc code=end
