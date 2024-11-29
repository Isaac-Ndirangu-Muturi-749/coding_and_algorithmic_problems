class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None  # Initialize the previous pointer as None
        current = head  # Start from the head node

        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the previous pointer to the current node
            current = next_node  # Move to the next node

        return prev  # Return the new head of the reversed list
