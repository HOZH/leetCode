#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def build(self, node, parent_val, left):

        if node:

            node.val = 2*parent_val+(1 if left else 2)
            self.set.add(node.val)

            self.build(node.left, node.val, True)
            self.build(node.right, node.val, False)

    def __init__(self, root: TreeNode):
        self.set = set()
        self.root = root
        self.build(root.left, 0, True)
        self.build(root.right, 0, False)

    def find(self, target: int) -> bool:

        return target in self.set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end
