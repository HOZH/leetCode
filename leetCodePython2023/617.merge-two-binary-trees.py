#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(a, b):
            if not a and not b:
                return None
            temp = 0
            if a:
                temp += a.val
            if b:
                temp += b.val
            new_left = helper(a.left if a else None, b.left if b else None)
            new_right = helper(a.right if a else None, b.right if b else None)
            return TreeNode(temp, new_left, new_right)

        return helper(root1, root2)


# @lc code=end
