#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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

        self.ans = None

        def helper(node, a, b, x, y, flag):

            # can add a determineter to end once the ans is found
            if node is None:
                return False, False

            if node == a:
                b = True
            if node == x:
                y = True

            left = helper(node.left, a, False, x, False, flag)
            right = helper(node.right, a, False, x, False, flag)

            b = True if(b or left[0] or right[0]) else False
            y = True if(y or left[1] or right[1]) else False

            if b and y:
                if self.ans is None:
                    self.ans = node

            return b, y

        helper(root, p, False, q, False, self.ans)
        return self.ans


# @lc code=end
