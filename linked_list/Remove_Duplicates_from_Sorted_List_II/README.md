To solve this problem, we can use a two-pointer technique to traverse the sorted linked list. As the list is already sorted, all duplicates will be adjacent. Our goal is to remove nodes with duplicate values, leaving only distinct values.

Here’s how we can approach it:

1. **Use a Dummy Node**: We use a dummy node to handle edge cases, like when the head itself contains duplicates. The dummy node will point to the original head, and its value does not affect the list.

2. **Pointer Traversal**: We'll traverse the list with two pointers:
   - `prev`: Points to the last non-duplicate node.
   - `current`: Moves through the list to detect duplicates.

3. **Skip Duplicates**: If we detect consecutive nodes with the same value, we'll skip all nodes with that value by moving the `current` pointer until we find a new value.

4. **Update Pointers**: After handling duplicates, we'll update the `prev` pointer to point to the new distinct value, ensuring that the list is correctly re-linked.

### Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Dummy node to handle edge cases
        dummy = ListNode(0, head)
        prev = dummy

        # Traverse the list with the current pointer
        current = head
        while current:
            # Check if the current node is a duplicate
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Link prev to the node after the last duplicate
                prev.next = current.next
            else:
                # No duplicate detected, move prev pointer
                prev = prev.next
            # Move current pointer to the next node
            current = current.next

        # Return the modified list, which starts from dummy's next
        return dummy.next
```

### Explanation:

1. **Dummy Node**:
   - We create a dummy node with a value of `0` and link it to the head of the list. This helps handle cases where the head might be part of the duplicates.
   - `prev` is initialized to the dummy node.

2. **Traversing with `current`**:
   - We move the `current` pointer through the list.
   - If `current` and `current.next` have the same value, we enter a loop to skip all nodes with that duplicate value by advancing `current` until we encounter a new value.

3. **Re-linking with `prev`**:
   - If duplicates were skipped, `prev.next` is updated to point to `current.next`, effectively removing all duplicate nodes.
   - If no duplicates were detected, `prev` simply moves forward.

4. **Edge Cases**:
   - If the list is empty or contains only one node, it will be returned as is.
   - If all nodes in the list are duplicates, the list will become empty.

### Example Walkthrough:

#### Example 1: `head = [1,2,3,3,4,4,5]`

- We detect duplicates at nodes with values `3` and `4`.
- The output list will be `[1,2,5]` after removing the duplicate values.

#### Example 2: `head = [1,1,1,2,3]`

- We detect duplicates at nodes with value `1`.
- The output list will be `[2,3]` after removing the duplicate `1` values.

### Time Complexity:

- **O(n)** where `n` is the number of nodes in the linked list. We traverse the list once, skipping duplicate nodes as we go.

### Space Complexity:

- **O(1)** because we are only using a few pointers and not any additional space proportional to the input size.



