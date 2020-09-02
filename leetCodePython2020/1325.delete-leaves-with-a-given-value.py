#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def helper(node):
            if not node:
                return True

            left_none = helper(node.left)
            right_none = helper(node.right)

            if left_none:
                node.left = None
            if right_none:
                node.right = None

            if left_none and right_none:
                if node.val == target:
                    return True

            return False

        helper(root)
        return None if (root.val == target and not root.left and not root.right)else root


# @lc code=end
