#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        # if root is None:
        #     return None

        # root.left = self.pruneTree(root.left)
        # root.right = self.pruneTree(root.right)

        # if root.val == 1 or root.left or root.right:
        #     return root
        # else:
        #     return None

        def post_order(node):
            if not node:
                return None
            left = post_order(node.left)
            right = post_order(node.right)

            if node.val != 1 and not left and not right:
                return None
            node.left = left
            node.right = right
            return node

        return post_order(root)

# @lc code=end
