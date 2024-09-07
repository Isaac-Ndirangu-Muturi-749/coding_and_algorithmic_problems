class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize the dummy head of the resulting list.
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists.
        while l1 or l2 or carry:
            # Get the current values.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and update the carry.
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in the lists.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
