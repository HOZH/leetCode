#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:

        self.result = 0

        def helper(node, current):

            if not node:
                return 0

            current = current+str(node.val)

            if node.left or node.right:
                if node.left:
                    helper(node.left, current)
                if node.right:
                    helper(node.right, current)

            else:
                self.result += int(current, 2)

        helper(root, '')
        return self.result


# @lc code=end
