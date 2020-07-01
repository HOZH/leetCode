#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        self.arr = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)

        inorder(root)

        return self.arr

# @lc code=end
