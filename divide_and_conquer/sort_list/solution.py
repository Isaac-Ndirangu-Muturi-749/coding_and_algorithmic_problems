class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node, return the head
        if not head or not head.next:
            return head

        # Split the list into two halves using the slow and fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the list into two parts
        mid = slow.next
        slow.next = None

        # Sort each half recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to act as a starting point for the merged list
        dummy = ListNode()
        current = dummy

        # Merge two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach the remaining elements from either list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        # Return the sorted list, starting from dummy's next node
        return dummy.next
