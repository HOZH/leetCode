#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(L, R):

            if not L and not R:
                return True

            if L and R and L.val == R.val:
                return helper(L.left, R.right) and helper(L.right, R.left)
            return False

        return helper(root, root)

        # using bfs for the iterative solution maybe


# @lc code=end
