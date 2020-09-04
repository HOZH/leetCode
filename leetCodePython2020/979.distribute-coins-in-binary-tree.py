#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(node):
            if not node:
                return 0
            left_val = helper(node.left)
            right_val = helper(node.right)
            current_val = node.val+left_val+right_val
            # how many coins needed to be conveyed to parent or get from parent
            # self.ans += abs(current_val-1)
            # how many steps subs needed
            self.ans += abs(left_val)+abs(right_val)
            return current_val-1

        helper(root)
        return self.ans


# @lc code=end
