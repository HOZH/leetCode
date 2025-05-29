#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pt = 0
        self.lis = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.lis.append(node.val)
            in_order(node.right)
        in_order(root)

    def next(self) -> int:
        self.pt += 1
        return self.lis[self.pt-1]

    def hasNext(self) -> bool:
        return self.pt < len(self.lis)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
