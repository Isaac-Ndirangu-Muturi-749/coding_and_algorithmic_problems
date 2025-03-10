# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        return self.mergeHelper(lists, 0, len(lists) - 1)
    
    def mergeHelper(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        leftMerged = self.mergeHelper(lists, left, mid)
        rightMerged = self.mergeHelper(lists, mid + 1, right)
        return self.mergeTwoLists(leftMerged, rightMerged)
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next

