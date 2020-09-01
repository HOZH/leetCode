#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        stack = deque()
        result = deque()
        if root:
            stack.append(root)
        while len(stack):
            current_len = len(stack)
            current_layer = []
            while current_len:
                current = stack.popleft()
                current_layer.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
                current_len -= 1
            result.appendleft(current_layer)

        return result


# @lc code=end
