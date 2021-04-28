#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:



        def helper(node,container):

            if not node:
                return

            helper(node.left,container)
            container.append(node.val)
            helper(node.right,container)


        list1,list2 = [],[]

        helper(root1,list1)
        helper(root2,list2)

        ans = []
        while list1 and list2:

            if list1[0]<list2[0]:
                ans.append(list1[0])
                list1=list1[1:]

            else:
                ans.append(list2[0])
                list2=list2[1:]

        
        ans+=list1
        ans+=list2

        return ans
        
# @lc code=end

