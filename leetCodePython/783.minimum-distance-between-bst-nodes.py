#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    current, difference = float('-inf'), float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        # If no root, return
        if not root:
            return root
        # Inorder traversal
        self.minDiffInBST(root.left)
        # Store minimum of current - prev, update current
        self.difference, self.current = min(
            self.difference, root.val-self.current), root.val
        self.minDiffInBST(root.right)
        # Return minimum difference
        return self.difference
            


        

