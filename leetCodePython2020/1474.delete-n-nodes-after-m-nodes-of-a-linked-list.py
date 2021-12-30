#
# @lc app=leetcode id=1474 lang=python3
#
# [1474] Delete N Nodes After M Nodes of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        skip, delete = m-1, n

        flag = False

        while current:
            if skip:
                skip -= 1
                current = current.next
            else:
                temp = current.next
                if temp == None:
                    break
                while delete:
                    temp = temp.next
                    if temp == None:
                        flag = True
                        break
                    delete -= 1

                current.next = temp
                skip = m
                delete = n
            if flag == True:
                break

        return head

# @lc code=end
