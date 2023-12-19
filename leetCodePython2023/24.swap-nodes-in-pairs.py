#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.next = head
        pre = self
        """
        1,2,3,4
        2,1,3,4
        2,1,4,3,None
        """
        while pre.next and pre.next.next:
            a = pre.next
            b= pre.next.next
            # pre.next is the node will be executed in the next loop
            # b.next = a and a.next = b.next means first node and sec node in the current try will be swap, and a.next points to the thrid node
            # it's like a->b->c => b->a->c 
            pre.next = b
            b.next, a.next = a,b.next
            pre = a 
            
        return self.next


        
# @lc code=end

