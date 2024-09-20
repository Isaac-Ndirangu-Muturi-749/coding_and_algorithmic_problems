# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to help build the merged list
        dummy = ListNode()
        # Pointer to track the current node in the new merged list
        current = dummy

        # Traverse both lists
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val <= list2.val:
                current.next = list1  # Append list1's node to the merged list
                list1 = list1.next    # Move list1's pointer to the next node
            else:
                current.next = list2  # Append list2's node to the merged list
                list2 = list2.next    # Move list2's pointer to the next node
            # Move the pointer of the merged list to the next node
            current = current.next

        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next
