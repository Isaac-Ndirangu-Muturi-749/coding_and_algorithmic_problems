# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Create a dummy node, which helps simplify edge cases like removing the head.
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Move first pointer `n+1` steps ahead to maintain the gap between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both first and second pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Now, second is just before the node to remove
        second.next = second.next.next

        # Return the new head, which is dummy.next
        return dummy.next
