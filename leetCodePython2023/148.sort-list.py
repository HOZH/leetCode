#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        arr = []
        while current is not None:
            arr.append(current.val)
            current = current.next
        arr.sort()
        
        if len(arr) == 0:
            return None
        answer = ListNode(arr[0])
        current = answer
        for i in arr[1:]:
            current.next = ListNode(i)
            current = current.next
        
        return answer


        
# @lc code=end

