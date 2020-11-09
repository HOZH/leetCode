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
        stack = deque()
        if root:
            stack.appendleft(root)

        while len(stack):
            current = stack.popleft()
            result.appendleft(current.val)

            if current.left:
                stack.appendleft(current.left)
            if current.right:
                stack.appendleft(current.right)

        return result


# @lc code=end
