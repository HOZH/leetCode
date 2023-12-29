#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = deque()
        stack = deque([root])

        while len(stack):
            layer_size = len(stack)
            current_layer_vals = []
            while layer_size != 0:
                current = stack.popleft()
                current_layer_vals.append(current.val)

                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

                layer_size -= 1
            ans.appendleft(current_layer_vals)

        return ans

# @lc code=end
