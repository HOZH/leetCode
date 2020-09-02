#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0
        self.ans = float('-inf')

        def helper(node):

            if not node:
                return 0

            left_sub = helper(node.left)
            right_sub = helper(node.right)
            local_dia = left_sub+right_sub+1
            self.ans = local_dia if local_dia > self.ans else self.ans

            return max(left_sub, right_sub)+1

        helper(root)
        return self.ans-1

# @lc code=end
