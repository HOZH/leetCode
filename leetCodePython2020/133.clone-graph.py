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


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        g = dict()

        def get_graph(current):

            g[current.val] = [i.val for i in current.neighbors]

            for i in current.neighbors:

                if i.val not in g:
                    get_graph(i)

        get_graph(node)

        nodes = dict()

        for node_val in g.keys():
            nodes[node_val] = Node(node_val, [])

        for key, values in g.items():

            nodes[key].neighbors = [nodes[i] for i in values]

        return nodes[1]


# @lc code=end
