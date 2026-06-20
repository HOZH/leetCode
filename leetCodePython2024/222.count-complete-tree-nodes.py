#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
               return 0
        self.layers = [0]
        queue = deque([root])

        while len(queue):
            current_layer_size = len(queue)
            current_layer_count = 0
            while current_layer_size:
                node = queue.popleft()
                # if node is not None:
                current_layer_count += 1
                if node.left:
                        queue.append(node.left)
                if node.right:
                        queue.append(node.right)
                current_layer_size -= 1
            self.layers.append(current_layer_count)

        return sum(self.layers)


# @lc code=end

                         1  # this is a complete tree
                    2         3 
                4                   5
            6                           7
