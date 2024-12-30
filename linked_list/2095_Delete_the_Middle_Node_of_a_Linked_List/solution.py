# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge case: If there's only one node, return None
        if not head or not head.next:
            return None

        # Initialize pointers
        slow = head
        fast = head
        prev = None  # To track the node before the middle node

        # Traverse the list to find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        if prev:
            prev.next = slow.next

        return head
