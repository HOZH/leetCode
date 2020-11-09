#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        self.result = []
        # def pre_order(node):

        #     if not node:
        #         return

        #     self.result.append(node.val)
        #     pre_order(node.left)
        #     pre_order(node.right)

        # pre_order(root)

        stack = deque()
        if root:
            stack.appendleft(root)

        # FILO stack
        while len(stack):
            current = stack.popleft()
            self.result.append(current.val)

            if current.right:
                stack.appendleft(current.right)
            if current.left:
                stack.appendleft(current.left)

        return self.result


# @lc code=end
