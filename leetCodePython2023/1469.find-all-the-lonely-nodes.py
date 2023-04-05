#
# @lc app=leetcode id=1469 lang=python3
#
# [1469] Find All The Lonely Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def helper(node,is_solo):
            if is_solo:
                self.ans.append(node.val)
            has_left = True if node.left else False
            has_right = True if node.right else False
            if has_left and not has_right:
                helper(node.left,True)
            elif has_right and not has_left:
                helper(node.right,True)
            elif has_right and has_left:
                helper(node.right,False)
                helper(node.left,False)
         
        helper(root,False)
        return self.ans


# @lc code=end
