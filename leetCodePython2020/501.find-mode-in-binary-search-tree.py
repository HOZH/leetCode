#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.arr = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)

        inorder(root)

        if len(self.arr) == 0:
            return None

        max_count = 1
        count = 1
        prev = self.arr[0]
        current = None
        result = []
        for i in range(1, len(self.arr)):
            if self.arr[i] == prev:
                count += 1

            else:
                count = 1
            prev = self.arr[i]

            if count > max_count:
                max_count = count

        count = 1
        prev = self.arr[0]
        for i in range(1, len(self.arr)):
            if self.arr[i] == prev:
                count += 1

            else:
                count = 1

            prev = self.arr[i]

            if count == max_count:
                result.append(self.arr[i])

        return self.arr if max_count == 1 else result


# @lc code=end
