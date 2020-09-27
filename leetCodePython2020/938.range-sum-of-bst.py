#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if L <= root.val <= R:
            result = root.val
        else:
            result = 0

        if L < root.val:
            if root.left:
                result += self.rangeSumBST(root.left, L, min(root.val, R))
        if R > root.val:
            if root.right:
                result += self.rangeSumBST(root.right, max(root.val, L), R)

        return result


# @lc code=end
