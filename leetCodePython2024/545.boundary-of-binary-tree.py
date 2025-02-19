#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # 判断是否为叶子节点
        def is_leaf(node):
            return not node.left and not node.right

        # 获取左边界
        def get_left_boundary(node):
            left_boundary = []
            while node:
                if not is_leaf(node):
                    left_boundary.append(node.val)
                node = node.left if node.left else node.right
            return left_boundary

        # 获取叶子节点
        def get_leaves(node, leaves):
            if not node:
                return
            if is_leaf(node):
                leaves.append(node.val)
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        # 获取右边界（逆序）
        def get_right_boundary(node):
            right_boundary = []
            while node:
                if not is_leaf(node):
                    right_boundary.append(node.val)
                node = node.right if node.right else node.left
            return right_boundary[::-1]  # 逆序

        # 1. 根节点
        result = [root.val] if not is_leaf(root) else []

        # 2. 左边界
        if root.left:
            result += get_left_boundary(root.left)

        # 3. 叶子节点
        get_leaves(root, result)

        # 4. 右边界（逆序）
        if root.right:
            result += get_right_boundary(root.right)

        return result
        
# @lc code=end

