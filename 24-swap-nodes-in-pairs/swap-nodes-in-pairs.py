# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = first.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next   