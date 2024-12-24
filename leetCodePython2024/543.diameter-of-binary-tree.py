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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0
            left_len, right_len = helper(node.left), helper(node.right)
            node.val = left_len+right_len+1
            return max(left_len, right_len)+1

        self.ans = 0

        def pre_order(node):
            if not node:
                return
            pre_order(node.left)
            self.ans = max(node.val, self.ans)
            pre_order(node.right)

        helper(root)
        pre_order(root)

        return self.ans-1


# @lc code=end
