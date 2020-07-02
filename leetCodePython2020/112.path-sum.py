#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # can be pruned by cutting off unpossible cases
        if root is None:
            return False

        if root.val == sum:
            if root.left is None and root.right is None:
                return True

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# @lc code=end
