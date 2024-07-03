#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
            in_order(node.right)

        in_order(root)
        return self.ans


# @lc code=end
