#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:

#     def helper(self, node, length):

#         if node:

#             left_len = self.helper(node.left, length+1)
#             right_len = self.helper(node.right, length+1)

#             return left_len if left_len > right_len else right_len

#         else:

#             if self.lower == -1 or length < self.lower:
#                 self.lower = length

#             return length

#     def isBalanced(self, root: TreeNode) -> bool:

#         self.lower = -1

#         a=self.helper(root, 0)
#         b=self.lower
#         print(a,b)

# no sure how the hell [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5] is high_balanced binary tree
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDep(node):
            if not node:
                return 0
            node.dep = 1 + max(getDep(node.left), getDep(node.right))
            return node.dep

        def checkValid(head):
            if not head or not head.left and not head.right:
                return True
            if not head.left:
                return head.right.dep == 1
            if not head.right:
                return head.left.dep == 1

            return abs(head.left.dep-head.right.dep) <= 1 and checkValid(head.left) and checkValid(head.right)

        getDep(root)
        return checkValid(root)
