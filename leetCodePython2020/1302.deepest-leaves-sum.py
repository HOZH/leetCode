#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.ans = defaultdict(int)
        self.result_key = -1

        def helper(node, level):
            if not node:
                return

            self.ans[level] += node.val
            self.result_key = level if level > self.result_key else self.result_key
            helper(node.left, level+1)
            helper(node.right, level+1)

        helper(root, 0)
        return self.ans[self.result_key]
        # return self.ans[max(self.ans.keys())]


# @lc code=end
