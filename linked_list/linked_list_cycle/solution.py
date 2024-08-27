class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Edge case: if the list is empty or has only one node without a cycle
        if not head or not head.next:
            return False

        slow = head
        fast = head

        # Move the slow and fast pointers through the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True

        # If we reach here, there's no cycle
        return False
