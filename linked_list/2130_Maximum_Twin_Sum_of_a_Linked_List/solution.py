# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Calculate twin sums and find the maximum
        max_twin_sum = 0
        first, second = head, prev
        while second:  # Iterate through both halves
            max_twin_sum = max(max_twin_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_twin_sum
