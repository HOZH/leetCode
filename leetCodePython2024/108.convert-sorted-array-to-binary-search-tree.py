#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return None
        m = (length - 1)//2
        left, right = nums[:m], nums[m+1:]
        node = ListNode(nums[m])
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node


# @lc code=end
