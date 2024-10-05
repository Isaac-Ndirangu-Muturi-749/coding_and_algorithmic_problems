# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node to handle edge cases
        dummy = ListNode(0, head)
        prev = dummy

        # Traverse the list with the current pointer
        current = head
        while current:
            # Check if the current node is a duplicate
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Link prev to the node after the last duplicate
                prev.next = current.next
            else:
                # No duplicate detected, move prev pointer
                prev = prev.next
            # Move current pointer to the next node
            current = current.next

        # Return the modified list, which starts from dummy's next
        return dummy.next
