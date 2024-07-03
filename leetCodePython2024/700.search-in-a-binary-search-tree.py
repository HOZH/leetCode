#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None

        def helper(node):
            if not node:
                return
            if node.val == val:
                self.ans = node
                return
            elif node.val > val:
                helper(node.left)
            else:
                helper(node.right)

        helper(root)
        return self.ans


# @lc code=end
