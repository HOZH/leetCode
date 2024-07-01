#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.in_order_list = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.in_order_list.append(node.val)
            in_order(node.right)
            
        in_order(root)

        return sum(list(filter(lambda x: high >= x >= low, self.in_order_list)))


# @lc code=end
