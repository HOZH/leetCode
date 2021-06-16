#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.count = 0

        def helper(node, max_val):

            if not node:
                return

            if node.val >= max_val:
                self.count += 1

            temp = max(node.val, max_val)

            helper(node.left,temp)
            helper(node.right,temp)

        helper(root, root.val)

        return self.count


# @lc code=end
