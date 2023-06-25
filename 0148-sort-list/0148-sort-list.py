# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow.next
        slow.next = None
        left = head
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        head = self.merge(left, right)
        return head

    def merge(self, left, right):
        if not right:
            return left
        if not left:
            return right

        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(right.next, left)
            return right





        