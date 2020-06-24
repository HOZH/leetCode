#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from heapq import heappush, heappop, heapify


class Solution:

    def ll_2_tuple(self, ll):
        result = []
        # head node
        current = ll
        while current is not None:
            result.append(current.val)
            current = current.next

        return tuple(result)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = []
        tuples = list(map(lambda x: self.ll_2_tuple(x), filter(
            lambda x: x is not None, lists)))
        heapify(tuples)

        while len(tuples) > 0:

            temp = heappop(tuples)
            result.append(temp[0])
            if len(temp) > 1:
                heappush(tuples, temp[1:])

        if len(result) < 1:
            return None

        else:

            head = ListNode(result[0])
            current = head

            for i in result[1:]:
                current.next = ListNode(i)
                current = current.next

            return head


# @lc code=end
