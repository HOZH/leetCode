#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    answer = str()


    def helper(self,t):
        if t is not None:
        
            self.answer += str(t.val)

            if t.left is None and t.right is None:

                pass

            elif t.right is None:
                self.answer += '('
                self.helper(t.left)
                self.answer += ')'

            elif t.left is None:

                self.answer += '()('
                self.helper(t.right)
                self.answer += ')'

            else:
                self.answer += '('
                self.helper(t.left)
                self.answer += ')('
                self.helper(t.right)
                self.answer += ')'




    def tree2str(self, t: TreeNode) -> str:

        self.helper(t)

        return self.answer

        

        
