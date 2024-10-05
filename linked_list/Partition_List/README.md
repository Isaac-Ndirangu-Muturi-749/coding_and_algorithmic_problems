To solve the problem of partitioning a linked list around a value `x`, we need to rearrange the list so that:
- All nodes with values less than `x` come before nodes with values greater than or equal to `x`.
- The relative order of the nodes in each partition must be preserved.

### Approach:
We can achieve this by creating two separate lists:
1. One list to hold nodes with values less than `x`.
2. Another list to hold nodes with values greater than or equal to `x`.

After processing the entire linked list, we will connect the two lists:
- The list with nodes less than `x` will be linked to the list with nodes greater than or equal to `x`.
- Finally, we return the head of the new merged list.

### Algorithm:
1. Initialize two dummy nodes, `less` and `greater`, which will serve as the heads of two new lists. We also maintain two pointers (`less_ptr` and `greater_ptr`) to build the lists.
2. Traverse the input list:
   - If a node's value is less than `x`, append it to the `less` list.
   - Otherwise, append it to the `greater` list.
3. Once all nodes are processed, link the `less` list to the `greater` list.
4. Return the head of the merged list, which will be the `less` list's dummy node's next pointer.

### Code Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two dummy nodes
        less_head = ListNode(0)  # List for nodes less than x
        greater_head = ListNode(0)  # List for nodes greater than or equal to x

        less_ptr = less_head  # Pointer for the less list
        greater_ptr = greater_head  # Pointer for the greater list

        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Append to the less list
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                # Append to the greater list
                greater_ptr.next = current
                greater_ptr = greater_ptr.next
            current = current.next

        # Terminate the greater list
        greater_ptr.next = None

        # Link the less list with the greater list
        less_ptr.next = greater_head.next

        # Return the merged list starting from less_head.next
        return less_head.next
```

### Explanation:
1. **Dummy Nodes**:
   - `less_head` and `greater_head` are dummy nodes to handle the case where the partition is empty.
   - `less_ptr` and `greater_ptr` are pointers that help us build the respective lists.

2. **Traverse the List**:
   - We iterate through the input list. For each node, we check if its value is less than `x`. If it is, we add it to the `less` list. Otherwise, we add it to the `greater` list.

3. **Link the Lists**:
   - After traversing the entire list, we link the `less` list to the `greater` list by setting `less_ptr.next` to `greater_head.next`.

4. **Termination**:
   - We explicitly terminate the `greater` list by setting `greater_ptr.next = None`, ensuring no cyclic references.

5. **Return the New Head**:
   - The new head of the partitioned list will be `less_head.next`.

### Time Complexity:
- **O(n)** where `n` is the number of nodes in the linked list. We traverse the list once.

### Space Complexity:
- **O(1)** since we only use a few pointers and dummy nodes, and we do not use any extra space proportional to the input size.

### Example Walkthrough:

#### Example 1:
- **Input**: `head = [1,4,3,2,5,2]`, `x = 3`
- **Steps**:
  - Initialize `less_head` and `greater_head`.
  - Traverse the list:
    - Node 1: Add to `less` list.
    - Node 4: Add to `greater` list.
    - Node 3: Add to `greater` list.
    - Node 2: Add to `less` list.
    - Node 5: Add to `greater` list.
    - Node 2: Add to `less` list.
  - Link `less` and `greater` lists.
  - **Output**: `[1, 2, 2, 4, 3, 5]`

#### Example 2:
- **Input**: `head = [2,1]`, `x = 2`
- **Steps**:
  - Node 2: Add to `greater` list.
  - Node 1: Add to `less` list.
  - Link `less` and `greater` lists.
  - **Output**: `[1, 2]`


