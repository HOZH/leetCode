#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def preorder(node, left):

            if not node:
                if left:
                    return 'ln.'
                else:
                    return 'rn.'

            return 'v'+str(node.val)+'v.'+preorder(node.left, True)+preorder(node.right, False)

        s_str = preorder(s, True)
        t_str = preorder(t, True)

        return False if s_str.find(t_str) < 0 else True

        # def helper(p, q):
        #     if p is None or q is None:
        #         return p == q

        #     if p.val != q.val:
        #         return False

        #     else:
        #         return helper(p.left, q.left) and helper(p.right, q.right)

        # if helper(s, t):
        #     return True

        # return (self.isSubtree(s.left, t) if s.left else False) or (self.isSubtree(s.right, t) if s.right else False)


# @lc code=end
