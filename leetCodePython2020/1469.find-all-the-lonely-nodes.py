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

            if not node.left or not node.right:
                if node.left:
                    self.ans.append(node.left.val)
                if node.right:
                    self.ans.append(node.right.val)

            helper(node.right)
            helper(node.left)

        helper(root)
        return self.ans


# @lc code=end
