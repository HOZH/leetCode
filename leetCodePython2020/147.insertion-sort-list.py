#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def insertionSortList_temp(self, head: ListNode) -> ListNode:

    #     if head is None or head.next is None:
    #         return head

    #     tail, current = head, head

    #     while current is not None:
    #         temp_current = head

    #         while temp_current is not tail:
    #             # print(temp_current is tail, temp_current.val, tail.val)
    #             if current.val < temp_current.val:

    #                 temp_val = temp_current.val

    #                 temp_current.val = current.val

    #                 # start pushing back vals by one position

    #                 while temp_current is not tail:

    #                     next_val = temp_current.next.val

    #                     temp_current.next.val = temp_val
    #                     temp_current = temp_current.next
    #                     temp_val = next_val

    #             else:
    #                 temp_current = temp_current.next

    #         tail = tail.next
    #         current = tail

    #     return head
    def insertionSortList_temp(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        temp_head = ListNode(-5001)
        temp_head.next = head

        current = head
        global_prev, global_next = temp_head, current.next

        while current is not None:
            temp_current, temp_prev = temp_head, None

            while temp_current != current:
                if temp_current is None:
                    temp_prev.next = current
                    current.next = None
                    global_prev.next = global_next
                    if global_next:

                        current = global_next
                        global_next = global_next.next
                    else:
                        current = None

                    break

                elif temp_current.val < current.val:
                    temp_prev = temp_current
                    temp_current = temp_current.next
                else:
                    temp_prev.next = current
                    current.next = temp_current
                    global_prev.next = global_next
                    if global_next:

                        current = global_next
                        global_next = global_next.next
                    else:
                        current = None

                    break
            if temp_current == current:
                global_prev = current
                if global_next:
                    current = global_next
                    global_next = global_next.next
                else:
                    break

        return temp_head.next

    def insertionSortList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        current, global_prev = head, None
        global_tail = head

        while current is not None:
            temp_current, prev = head, None
            if current.val < head.val:
                head = ListNode(current.val, head)
                global_prev.next = current.next
                current = global_prev

            elif current.val > global_tail.val:
                pass

            else:

                while temp_current is not current:
                    if current.val < temp_current.val:
                        if prev:
                            prev.next = ListNode(current.val, temp_current)

                        else:
                            head = ListNode(current.val, head)

                        global_prev.next = current.next

                        current = global_prev
                        break

                    else:
                        prev, temp_current = temp_current, temp_current.next

            global_prev, current = current, current.next
            global_tail = global_prev

        return head

# @lc code=end
