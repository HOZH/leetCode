#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_list = []

        def pre_order_helper(node):
            if node:
                self.flatten_list.append(node.val)
                pre_order_helper(node.left)
                pre_order_helper(node.right)

        def fill(node):
            if node:
                elements_left = len(self.flatten_list)
                if elements_left:
                    current = self.flatten_list.pop(0)
                    node.val = current
                    node.left = None
                    if elements_left > 1:
                        if not node.right:
                            node.right = TreeNode()
                        fill(node.right)

        pre_order_helper(root)
        fill(root)

# @lc code=end

