To detect if there is a cycle in a linked list, we can use Floyd's Tortoise and Hare algorithm (also known as the two-pointer technique). This algorithm uses two pointers: a slow pointer (the tortoise) and a fast pointer (the hare). The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle, these two pointers will eventually meet; if there is no cycle, the fast pointer will reach the end of the list.

### Algorithm Explanation:
1. **Initialization**:
   - We initialize two pointers, `slow` and `fast`, both starting at the head of the list.
2. **Movement**:
   - The `slow` pointer moves one step at a time (`slow = slow.next`), while the `fast` pointer moves two steps at a time (`fast = fast.next.next`).
3. **Cycle Detection**:
   - If the `fast` pointer reaches the end (`None`), there is no cycle.
   - If there is a cycle, the `slow` and `fast` pointers will eventually meet at some node inside the cycle.

### Code Implementation:

```python
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
```

### Example Usage:

#### Example 1:
- **Input**: `head = [3,2,0,-4], pos = 1`
- **Output**: `True`
- **Explanation**: There is a cycle in the linked list where the tail connects to the 1st node (0-indexed).

#### Example 2:
- **Input**: `head = [1,2], pos = 0`
- **Output**: `True`
- **Explanation**: There is a cycle in the linked list where the tail connects to the 0th node.

#### Example 3:
- **Input**: `head = [1], pos = -1`
- **Output**: `False`
- **Explanation**: There is no cycle in the linked list.

### Time and Space Complexity:
- **Time Complexity**: `O(n)`, where `n` is the number of nodes in the linked list. In the worst case, we might visit all nodes once.
- **Space Complexity**: `O(1)` since we are using only two pointers regardless of the number of nodes.

This algorithm provides an efficient solution with constant space and linear time complexity.
