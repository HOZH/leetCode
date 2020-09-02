#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

        # self.answer = None
        # if p.val > q.val:
        #     p, q = q, p

        # def helper(node, a, b):

        #     if self.answer:
        #         return True, True
        #     if not node:
        #         return False, False

        #     a = node.val == p.val
        #     b = node.val == q.val

        #     if not a:
        #         temp_a, temp_b = helper(node.left, False, False)
        #         a |= temp_a
        #         b |= temp_b
        #     if not b:
        #         temp_a, temp_b = helper(node.right, False, False)
        #         a |= temp_a
        #         b |= temp_b

        #     if a and b and not self.answer:
        #         self.answer = node

        #     return a, b

        # helper(root, False, False)
        # return self.answer


# @lc code=end
