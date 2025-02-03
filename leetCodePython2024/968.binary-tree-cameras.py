#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # bottom up greedy search
        self.count = 0

        # dfs
        # covered, cover other
        # True,False
        # True,True
        # False,False

        def postorder(node):

            if node is None:
                return None

            left = postorder(node.left)

            right = postorder(node.right)

            # set up a camera at current node
            # if any of its children needs support from it
            if (left and left[0] == False) or (right and right[0] == False):
                self.count += 1
                return True, True

            # case leaves included here
            # true if and only if current node is a leave or none of its children supports it
            elif ((left[1] == False) if left else True) and ((right[1] == False) if right else True):
                return False, False

            # case where current node is taking care by any of its children
            else:
                return True, False

        temp = postorder(root)
        if temp[0] == False:
            self.count += 1

        return self.count
        
# @lc code=end

