#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(node, local_max, local_min, is_root):

            if not node:
                return
            if not is_root:
                self.ans = max(self.ans, abs(node.val-local_max),
                               abs(node.val-local_min))

            helper(node.left, max(local_max, node.val), min(local_min, node.val,
                                                            ), False)
            helper(node.right, max(local_max, node.val), min(local_min, node.val,
                                                             ), False)

        helper(root, -1, 10e6, True)

        return self.ans


# @lc code=end
