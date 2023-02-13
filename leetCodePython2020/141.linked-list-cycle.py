#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return None
        pt1, pt2 = head, head
        
        while True:
            pt1 = None if not pt1 else pt1.next
            pt2 = None if not pt2 or not pt2.next else pt2.next.next

            if pt1 == pt2:
                if pt1 is not None:
                    return True
                else:
                    return False

# @lc code=end
