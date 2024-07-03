#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.sec = None, None
        self.prev = None

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev is not None:
                if self.prev.val > node.val:
                    if self.first is None:
                        self.first = self.prev
                    self.sec = node

            self.prev = node
            in_order(node.right)

        in_order(root)
        self.first.val, self.sec.val = self.sec.val, self.first.val


# @lc code=end
