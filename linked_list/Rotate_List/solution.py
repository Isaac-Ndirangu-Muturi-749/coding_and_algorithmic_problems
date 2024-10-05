# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and get to the last node
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Step 2: Make the list circular
        current.next = head

        # Step 3: Calculate the new head position (after n - k % n nodes)
        k = k % length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        # Step 4: Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
