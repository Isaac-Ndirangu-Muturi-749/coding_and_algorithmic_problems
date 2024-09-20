To merge two sorted linked lists, you can use an iterative approach where you compare the nodes of both lists and append the smaller one to a new linked list. This will ensure that the final linked list is also sorted.

### Approach:

1. **Create a dummy node**: This will be the starting point for the new merged list. The dummy node helps in easily managing the head of the new list without worrying about special cases like an empty list.
2. **Iterate through both lists**: Compare the nodes from `list1` and `list2`. Append the smaller node to the merged list and move the pointer of that list to the next node.
3. **Add the remaining nodes**: Once one list is fully traversed, append the remaining nodes of the other list to the merged list.
4. **Return the merged list**: The head of the merged list will be the next node of the dummy node (since the dummy node was just a placeholder).

### Code Implementation:

```python
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
```

### Explanation:

1. **ListNode Class**: This is a basic definition for a singly-linked list node. Each node contains a `val` (the value of the node) and a `next` pointer to the next node.
2. **mergeTwoLists Method**:
   - A dummy node is created to facilitate merging without worrying about edge cases.
   - The `while` loop runs as long as both `list1` and `list2` have nodes. In each iteration, the smaller node is appended to the merged list.
   - Once one list is exhausted, the remaining nodes of the other list are directly appended since the list is already sorted.
   - Finally, the function returns the merged list starting from `dummy.next`.

### Example Walkthrough:

**Example 1:**

Input:
```
list1 = [1,2,4]
list2 = [1,3,4]
```

1. Start with dummy node: `dummy -> None`
2. Compare `1 (list1)` and `1 (list2)`, append `1 (list1)`:
   ```
   dummy -> 1 -> None
   list1 moves to 2
   ```
3. Compare `2 (list1)` and `1 (list2)`, append `1 (list2)`:
   ```
   dummy -> 1 -> 1 -> None
   list2 moves to 3
   ```
4. Compare `2 (list1)` and `3 (list2)`, append `2 (list1)`:
   ```
   dummy -> 1 -> 1 -> 2 -> None
   list1 moves to 4
   ```
5. Compare `4 (list1)` and `3 (list2)`, append `3 (list2)`:
   ```
   dummy -> 1 -> 1 -> 2 -> 3 -> None
   list2 moves to 4
   ```
6. Compare `4 (list1)` and `4 (list2)`, append `4 (list1)`:
   ```
   dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> None
   list1 becomes None
   ```
7. Since `list1` is empty, append remaining `4 (list2)`:
   ```
   dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
   ```

Output:
```
[1,1,2,3,4,4]
```

**Example 2:**

Input:
```
list1 = [], list2 = [0]
```

Since `list1` is empty, directly append `list2`:
```
dummy -> 0 -> None
```

Output:
```
[0]
```

### Time and Space Complexity:

- **Time Complexity**: O(n + m), where `n` is the length of `list1` and `m` is the length of `list2`. We traverse both lists exactly once.
- **Space Complexity**: O(1) in terms of auxiliary space, as the merging is done in-place (without using extra space other than a few pointers). However, the space used by the linked list nodes themselves is still O(n + m).
