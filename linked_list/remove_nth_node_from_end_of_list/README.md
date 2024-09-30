To solve the problem of removing the nth node from the end of a singly linked list in one pass, we can use the **two-pointer technique**. The idea is to move one pointer ahead by `n` steps, and then move both pointers together until the first pointer reaches the end of the list. This way, the second pointer will point to the node just before the one we want to remove.

### Approach:
1. Use two pointers: `first` and `second`. Initially, both point to the head of the list.
2. Move the `first` pointer `n` steps ahead.
3. Then move both `first` and `second` together until the `first` pointer reaches the end of the list.
4. Now, the `second` pointer will be just before the node we want to remove. Update the next pointer of the `second` node to skip the `nth` node.
5. Return the head of the modified list.

If `n` is equal to the length of the list, the node to be removed is the head. In this case, we just return the next node after the head.

### Code Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node, which helps simplify edge cases like removing the head.
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Move first pointer `n+1` steps ahead to maintain the gap between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both first and second pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Now, second is just before the node to remove
        second.next = second.next.next

        # Return the new head, which is dummy.next
        return dummy.next
```

### Explanation:
1. **Dummy Node**: We use a dummy node that points to the head of the list to handle edge cases, like removing the head itself. This avoids needing special logic for those cases.

2. **Two-Pointer Movement**:
   - Move the `first` pointer `n+1` steps forward, where `n` is the node from the end to be removed.
   - Then, move both pointers (`first` and `second`) together. This ensures that when `first` reaches the end, `second` is just before the node to remove.

3. **Removal**: After reaching the node to remove, we change the `next` pointer of the `second` node to skip the target node (`second.next.next`).

4. **Return**: Return `dummy.next` as the head of the modified list.

### Example Walkthrough:

- **Example 1**:
    ```plaintext
    Input: head = [1,2,3,4,5], n = 2
    First moves 3 steps forward.
    Second moves to the node before the target (node 3).
    Output: [1,2,3,5]
    ```
- **Example 2**:
    ```plaintext
    Input: head = [1], n = 1
    First moves 1 step forward, and second points to the dummy node.
    The head node is removed.
    Output: []
    ```

### Time and Space Complexity:
- **Time Complexity**: O(L), where `L` is the length of the linked list, since we only traverse the list once.
- **Space Complexity**: O(1), since we use a constant amount of extra space.

This approach ensures that the problem is solved in one pass with optimal space usage.
