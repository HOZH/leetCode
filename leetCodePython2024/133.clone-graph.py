#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque, defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        graph_dict = {}
        discovered = deque([node])

        while len(discovered):
            current_layer_len = len(discovered)
            while current_layer_len:
                current_layer_len -= 1
                current = discovered.popleft()
                if current.val not in graph_dict:
                    current_neighbors = current.neighbors
                    discovered.extend(current_neighbors)
                    graph_dict[current.val] = list(
                        map(lambda x: x.val, current.neighbors))

        nodes = dict()

        for i in range(1, len(graph_dict)+1):
            nodes[i] = Node(i, [])
        for i in range(1, len(graph_dict)+1):
            nodes[i].neighbors.extend(
                list(map(lambda x: nodes[x], graph_dict[i])))

        return nodes[1]
        
# @lc code=end

