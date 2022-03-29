#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        self.to_delete = set(to_delete)
        self.result = []

        def helper(node):
            if not node:
                return None

            if node.val in self.to_delete:
                left = helper(node.left)
                right = helper(node.right)
                if left:
                    self.result.append(left)
                if right:
                    self.result.append(right)
                return None
            else:
                node.left = helper(node.left)
                node.right = helper(node.right)
                return node

        temp = helper(root)
        if temp:
            self.result.append(temp)
        return self.result
            


# @lc code=end

