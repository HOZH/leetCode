#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start

from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        temp = defaultdict(int)

        for _, _to in edges:

            temp[_to] += 1

        result = set()

        for node, _ in edges:

            if node not in temp:

                result.add(node)

        return list(result)


# @lc code=end
