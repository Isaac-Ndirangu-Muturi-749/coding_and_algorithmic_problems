# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Create two dummy nodes
        less_head = ListNode(0)  # List for nodes less than x
        greater_head = ListNode(0)  # List for nodes greater than or equal to x

        less_ptr = less_head  # Pointer for the less list
        greater_ptr = greater_head  # Pointer for the greater list

        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Append to the less list
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                # Append to the greater list
                greater_ptr.next = current
                greater_ptr = greater_ptr.next
            current = current.next

        # Terminate the greater list
        greater_ptr.next = None

        # Link the less list with the greater list
        less_ptr.next = greater_head.next

        # Return the merged list starting from less_head.next
        return less_head.next
