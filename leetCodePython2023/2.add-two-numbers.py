#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = 0,0
        digit = 0
        while l1!=None:
            num1+=10**digit*l1.val
            digit+=1
            l1=l1.next

        digit = 0
        while l2!=None:
            num2+=10**digit*l2.val
            digit+=1
            l2=l2.next
        temp = [*str(num1+num2)][::-1]
        head = ListNode()
        node =head
        for i in range(len(temp)):
            node.next=ListNode(int(temp[i])) 
            node=node.next

        return head.next
            
        
        
# @lc code=end

