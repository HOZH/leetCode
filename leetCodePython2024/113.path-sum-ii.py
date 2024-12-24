#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        def helper(node, current_val, current_list):
            if node.left is None and node.right is None and current_val+node.val == targetSum:
                self.ans.append(current_list+[node.val])
                return
            if node.left:
                helper(node.left, current_val+node.val,
                       current_list+[node.val])
            if node.right:
                helper(node.right, current_val+node.val,
                       current_list+[node.val])
        if not root:
            return []
        helper(root, 0, [])

        return self.ans


# @lc code=end
