#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start


class MyLinkedList:
    class ListNode:

        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1

        result = self.head

        for i in range(index):
            result = result.next

        return result.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = self.ListNode(val, None, None)
            self.tail = self.head
        else:
            temp = self.ListNode(val, None, self.head)
            self.head.prev = temp
            self.head = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        if self.head is None:
            self.head = self.ListNode(val, None, None)
            self.tail = self.head

        else:
            temp = self.ListNode(val, self.tail, None)
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return

        elif index == self.length:
            return self.addAtTail(val)

        else:
            current = self.head
            for i in range(index):
                current = current.next
            temp = self.ListNode(val, current.prev, current)

            if index != 0:
                current.prev.next = temp
                current.prev = temp

            else:
                current.prev = temp
                self.head = temp

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.length:
            return

        elif index == self.length - 1:

            self.tail = self.tail.prev
            if self.length != 1:
                self.tail.next = None

        else:
            current = self.head
            for i in range(index):
                current = current.next
            if index != 0:
                current.prev.next = current.next

            else:
                self.head = current.next
            current.next.prev = current.prev

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
