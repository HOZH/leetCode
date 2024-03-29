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
            layer_size = len(stack)
            current_layer_vals = []
            while layer_size != 0:
                current = stack.popleft()
                current_layer_vals.append(current.val)

                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

                layer_size -= 1
            ans.append(current_layer_vals)

        return ans


# @lc code=end
