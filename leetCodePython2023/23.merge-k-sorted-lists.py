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

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        self.head = ListNode()
        self.current = self.head

        def ll_to_list(node):
            liz = []
            while node:
                liz.append(node.val)
                node = node.next

            return liz

        heap = []
        for i in lists:
            temp = ll_to_list(i)
            if len(temp) !=0:
                heappush(heap, temp)

        while len(heap) != 0:
            temp = heappop(heap)
            self.current.next = ListNode()
            self.current = self.current.next
            self.current.val = temp[0]

            temp = temp[1:]
            if len(temp) != 0:
                heappush(heap, temp)

        return self.head.next


# @lc code=end
