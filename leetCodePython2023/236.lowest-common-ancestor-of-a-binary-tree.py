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

        def seek_lca(node):

            if not node or self.ans != None:
                return False, False
            left_seek, right_seek = seek_lca(node.left), seek_lca(node.right)

            p_found = p.val == node.val or left_seek[0] or right_seek[0]
            q_found = q.val == node.val or left_seek[1] or right_seek[1]

            if p_found and q_found and self.ans is None:
                self.ans = node

            return p_found, q_found

        seek_lca(root)
        return self.ans


# @lc code=end
