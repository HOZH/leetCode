#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, current, target, relative_depth, parent):

        if current is None:
            return None

        if current.val != target:

            temp = self.helper(current.left, target,
                               relative_depth+1, current.val)

            return temp if temp is not None else self.helper(current.right, target, relative_depth+1, current.val)

        else:

            
            return (relative_depth, parent)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        a = self.helper(root, x, 0, None)
        b = self.helper(root, y, 0, None)

        if a is None or b is None:

            return False
        
        else:
            return True if (a[0] == b[0] and a[1] !=b[1]) else False
       
