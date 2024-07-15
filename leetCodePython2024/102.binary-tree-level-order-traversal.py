#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = deque([root])
        while len(stack):
            current_layer_len = len(stack)
            current_val_layer = []
            while current_layer_len:
                current_node = stack.popleft()
                if current_node.left:
                    stack.append(current_node.left)
                if current_node.right:
                    stack.append(current_node.right)

                current_val_layer.append(current_node.val)
                current_layer_len -= 1

            if len(current_val_layer) > 0:
                ans.append(current_val_layer)

        return ans


# @lc code=end
