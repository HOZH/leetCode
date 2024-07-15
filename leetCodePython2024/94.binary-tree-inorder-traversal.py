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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.ans.append(node.val)
            in_order(node.right)

        in_order(root)
        return self.ans

# @lc code=end
