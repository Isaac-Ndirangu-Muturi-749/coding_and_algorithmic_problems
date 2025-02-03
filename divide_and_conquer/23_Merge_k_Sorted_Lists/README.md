Optimized Solution: Merging K Sorted Linked Lists

We can efficiently merge K sorted linked lists using a min-heap (priority queue), which ensures that we always extract the smallest element among the current heads of the lists.


---

Efficient Approach (Using Min-Heap)

We push the head of each linked list into a min-heap (priority queue).

At each step, extract the smallest node from the heap and attach it to the merged list.

Push the next node (if available) from the same list into the heap.

Repeat until all nodes are merged.


Time Complexity:

Heap operations: O(log k) (insert & remove).

Total nodes: N (sum of all elements across all lists).

Total complexity: O(N log k) (since each node is inserted/extracted once).



---

Python Code Implementation

from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val  # Define comparison for heap sorting

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push initial nodes into the heap
        for l in lists:
            if l:
                heappush(min_heap, l)
        
        dummy = ListNode()  # Dummy node to simplify merging
        current = dummy
        
        while min_heap:
            # Get the smallest node
            node = heappop(min_heap)
            current.next = node
            current = node
            
            # Push the next node from the same list (if available)
            if node.next:
                heappush(min_heap, node.next)
        
        return dummy.next  # Return merged list starting from dummy's next


---

Explanation

1. Initialize a min-heap (min_heap = []).


2. Push the head of each non-empty linked list into the heap.


3. Extract the smallest element, attach it to the result list, and push the next node (if any) into the heap.


4. Repeat until all nodes are merged.




---

Alternative Approach: Divide and Conquer (O(N log K))

Another efficient approach is merge-sort style merging:

1. Pair-wise merge lists using merge two sorted lists technique.


2. Recursively divide and merge, reducing lists from K → K/2 → K/4 ... → 1.


3. Time Complexity: O(N log K) (since each level reduces by half).



Code for Divide and Conquer

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


---

Comparison of Methods

Both approaches are optimal, and min-heap is easier to implement when working with linked lists.

🚀 Choose heap for simplicity, merge-sort for in-place merging!

