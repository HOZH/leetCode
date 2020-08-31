#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        result = deque()
        stack = []
        if root:
            stack.append(root)

        while len(stack):
            current = stack.pop()
            result.appendleft(current.val)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return result


# @lc code=end
