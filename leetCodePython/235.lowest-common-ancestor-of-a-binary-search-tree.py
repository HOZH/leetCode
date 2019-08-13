#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, node, p, q):

        if node:

            a = self.helper(node.left, p, q)

            b = self.helper(node.right, p, q)

            if type(a) is TreeNode:
                return a

            elif type(b) is TreeNode:
                return b

            if node == p or node == q:

                if a == True or b == True:

                    return node
                else:

                    return True

            if a == True and b == True:

                return node

            elif b == True or a == True:

                return True

            else:

                return False

        else:

            return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        a = self.helper(root, p, q)

        return None if type(a) is not TreeNode else a
