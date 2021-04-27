#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(node, parent_flag, flag):

            if not node:
                return

            helper(node.left, node.val % 2 == 0, parent_flag)

            helper(node.right, node.val % 2 == 0, parent_flag)

            self.ans += node.val if flag else 0

        helper(root, False, False)

        return self.ans


# @lc code=end
