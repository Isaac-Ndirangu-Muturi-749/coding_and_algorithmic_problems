# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Step 1: Count the number of nodes in the list
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Step 2: Create dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy  # Pointer to the end of the last reversed group
        current = head

        # Step 3: Reverse nodes in groups of k
        while count >= k:
            prev = None
            tail = current  # The tail of the current group

            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect previous group's end to the reversed segment
            prev_group_end.next = prev
            tail.next = current  # Connect tail of reversed segment to the remaining list

            # Update pointers for the next group
            prev_group_end = tail
            count -= k

        return dummy.next  # The new head of the reversed list

