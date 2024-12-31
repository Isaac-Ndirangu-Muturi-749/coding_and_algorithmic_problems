# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # Store the head of the even list

        while even and even.next:
            # Move odd pointer to the next odd node
            odd.next = even.next
            odd = odd.next

            # Move even pointer to the next even node
            even.next = odd.next
            even = even.next

        # Connect the odd list to the even list
        odd.next = even_head

        return head
