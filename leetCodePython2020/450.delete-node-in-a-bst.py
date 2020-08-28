#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def deleteNode_1(self, root: TreeNode, key: int) -> TreeNode:

    #     if root is None:
    #         return root

    #     if key < root.val:
    #         root.left = self.deleteNode_1(root.left, key)
    #         return root

    #     elif key > root.val:
    #         root.right = self.deleteNode_1(root.right, key)
    #         return root

    #     else:
    #         # case root.val == key

    #         if root.left is None and root.right is None:
    #             return None

    #         elif root.left is None or root.right is None:
    #             return root.right if root.left is None else root.left

    #         else:

    #             if root.right == None:
    #                 replacement = root.left
    #                 while replacement.right:
    #                     replacement = replacement.right

    #                 root.val = replacement.val
    #                 root.left = self.deleteNode_1(root.left, root.val)

    #             else:

    #                 replacement = root.right

    #                 while replacement.left:
    #                     replacement = replacement.left

    #                 root.val = replacement.val
    #                 root.right = self.deleteNode_1(root.right, root.val)

    #             return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        else:
            # case root.val == key

            # case no sub nodes -> just delete the node
            if root.left is None and root.right is None:
                return None

            # case one of the node is none -> just concatnate the remaining fork
            elif root.left is None or root.right is None:
                return root.right if root.left is None else root.left

            # case both sub fork exsit
            else:

                replacement = root.right
                parent = root

                while replacement.left:
                    parent = replacement
                    replacement = replacement.left

                temp_right = replacement.right

                # root.left sub-tree always only contains eles samller or equal to replacement
                replacement.left = root.left
                # avoid cycle
                if root.right != replacement:
                    replacement.right = root.right

                # connect replacement's right sub-tree and replacement's parent node
                parent.left = temp_right
                return replacement


# @lc code=end
