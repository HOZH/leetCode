#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    total=0



    def convertBST(self, root: TreeNode) -> TreeNode:

        if root is not None:

            self.convertBST(root.right)

            self.total+=root.val

            root.val=self.total


            self.convertBST(root.left)


        return root




        

