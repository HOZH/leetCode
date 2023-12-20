#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False

            is_left_valid, is_right_valid = False, False
            if not node.left:
                is_left_valid = True
            else:
                is_left_valid = helper(node.left, min_val, node.val)

            if not node.right:
                is_right_valid = True
            else:
                is_right_valid = helper(node.right, node.val, max_val)

            return is_left_valid and is_right_valid

        return helper(root, float('-inf'), float('inf'))


# @lc code=end
