# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Edge case: If the list is empty or there's nothing to reverse
        if not head or left == right:
            return head

        # Step 1: Initialize a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Move `prev` to the node just before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Reverse the sublist from left to right
        # `start` is the first node to be reversed, `then` is the node after `start`
        start = prev.next
        then = start.next

        # Reverse the sublist by adjusting pointers
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        # Step 4: Return the new head of the list
        return dummy.next
