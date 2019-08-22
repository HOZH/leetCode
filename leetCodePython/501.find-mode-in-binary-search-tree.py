#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findMode(self, root: TreeNode) -> List[int]:

        lis = list()

        def helper(node):

            if node:

                nonlocal lis
                lis.append(node.val)

                helper(node.left)
                helper(node.right)

        helper(root)

        if len(lis) == 0:
            return[]
        a = collections.Counter(lis)
        max_count = a.most_common(1)[0][1]

        return list(filter(lambda x: a[x] == max_count, a))
