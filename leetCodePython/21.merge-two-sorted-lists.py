#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        v = []
        while l1:
            v.append(l1.val)
            l1 = l1.next
        while l2:
            v.append(l2.val)
            l2 = l2.next
        v.sort()
        res = ListNode(v[0])
        node = res
        for i in range(1, len(v)):
            node.next = ListNode(v[i])
            node = node.next
        return res

# class Solution:

#     init = list()

#     answer = ListNode(999)

#     def helper(self, node):

#         if node:

#             self.init.append(node.val)

#             self.helper(node.next)

#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

#         self.helper(l1)
#         self.helper(l2)

#         if len(self.init) == 0:
#             return None

#         self.init.sort()

#         res = ListNode(self.init[0])
#         node = res

#         for i in range(1, len(self.init)):

#             node.next = ListNode(self.init[i])
#             node = node.next

#         return res
