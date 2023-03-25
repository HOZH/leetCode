#
# @lc app=leetcode id=1485 lang=python3
#
# [1485] Clone Binary Tree With Random Pointer
#

# @lc code=start
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        memo = {}

        def dfs(node):
            if not node:
                return None
            if node not in memo:
                memo[node] = NodeCopy(node.val)
                memo[node].left = dfs(node.left)
                memo[node].right = dfs(node.right)
                memo[node].random = dfs(node.random)

            return memo[node]

        return dfs(root)


# @lc code=end
