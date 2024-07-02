#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def lis_to_tuple(node):
            lis = []
            while node:
                lis.append(node.val)
                node = node.next
            return lis

        queue = [lis_to_tuple(i) for i in lists]
        queue = list(filter(lambda x: len(x) > 0, queue))
        if not len(queue):
            return None
        heapify(queue)
        ans_lis = []
        while len(queue):
            current_lis = heappop(queue)
            ans_lis.append(current_lis[0])
            current_lis = current_lis[1:]
            if len(current_lis) > 0:
                heappush(queue, current_lis)

        head = ListNode(None)
        current = head
        for i in ans_lis:
            current.next = ListNode(i)
            current = current.next

        return head.next


# @lc code=end
