# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        """
        1. 2 pointer: 1 to the mid, 1 to the end
        2. reverse on part
        3. compare 
        
        """
        tail_count = mid_count = 1
        p_tail = p_mid = head
        while p_tail.next!=None:
            p_tail = p_tail.next
            tail_count+=1
        while mid_count<tail_count//2:
            p_mid = p_mid.next
            mid_count+=1
        
        
        """reverse mid-tail"""
        second_mid = p_mid.next
        p_prev = None
        while second_mid.next!=None:
            p_next = second_mid.next
            second_mid.prev = p_prev
            p_prev = second_mid
            second_mid = p_next
        
        
        """compare second_mid -> p_mid vs head -> p_mid"""
        p_left = head
        p_right = p_tail
        mid_count = 0
        while mid_count<tail_count//2:
            if p_left.val!=p_right.val:
                return False
            mid_count+=1
        return True
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True