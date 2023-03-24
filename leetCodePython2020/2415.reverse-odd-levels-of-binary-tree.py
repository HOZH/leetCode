#
# @lc app=leetcode id=2415 lang=python3
#
# [2415] Reverse Odd Levels of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        flag = False
        bag = deque([root])

        while len(bag):
            current_layer_len = len(bag)
            prev_layer = []
            prev_vals = []

            while current_layer_len > 0:
                current_layer_len -= 1
                current = bag.popleft()
                if flag:
                    prev_layer.append(current)
                    prev_vals.append(current.val)
                if current.left:
                    bag.append(current.left)
                if current.right:
                    bag.append(current.right)
            if flag:
                prev_vals = prev_vals[::-1]
                for i in range(len(prev_layer)):
                    prev_layer[i].val = prev_vals[i]
            flag = not flag

        return root


# @lc code=end
