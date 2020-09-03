#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import functools


class Solution:
    # @functools.lru_cache(None)
    def rob(self, root: TreeNode) -> int:

        def helper(node):

            if not node:
                return 0, 0, 0

            l, ll, lr = helper(node.left)
            r, rl, rr = helper(node.right)

            return max(node.val+ll+lr+rl+rr, l+r), l, r

        return helper(root)[0]

        # if not root:
        #     return 0

        # ll, lr, rl, rr = 0, 0, 0, 0

        # if root.left:
        #     ll, lr = self.rob(root.left.left), self.rob(root.left.right)

        # if root.right:
        #     rl, rr = self.rob(root.right.left), self.rob(
        #         root.right.right)

        # return max(root.val+ll+lr+rl+rr, self.rob(root.left)+self.rob(root.right))

# @lc code=end
