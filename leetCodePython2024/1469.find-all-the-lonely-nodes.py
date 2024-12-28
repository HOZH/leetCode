#
# @lc app=leetcode id=1469 lang=python3
#
# [1469] Find All The Lonely Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def helper(node):
            if not node:
                return
            left, right = node.left, node.right
            if (left and not right) or (right and not left):
                self.ans.append(left.val if left else right.val)
            helper(left)
            helper(right)

        helper(root)
        return self.ans

# @lc code=end
