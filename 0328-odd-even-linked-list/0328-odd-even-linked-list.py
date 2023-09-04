# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node1 = head
        if not node1:
            return node1
        newHead = node1
        node2 = head.next
        newTail = node2

        tmp = None
        if node2:
            tmp = node2.next
            node2.next = None

        node1.next = None
        

        while(tmp):
            node1.next = tmp
            tmp = tmp.next
            node1 = node1.next
            node1.next = None

            if tmp:
                node2.next = tmp
                tmp = tmp.next
                node2 = node2.next
                node2.next = None

        node1.next = newTail

        return newHead
        