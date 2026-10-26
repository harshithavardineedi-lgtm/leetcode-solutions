# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head

        while current:
            if current.child:
                child = current.child
                next_node = current.next

                current.next = child
                child.prev = current
                current.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                if next_node:
                    tail.next = next_node
                    next_node.prev = tail

            current = current.next

        return head