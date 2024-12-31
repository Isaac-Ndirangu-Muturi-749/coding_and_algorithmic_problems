To solve the problem of grouping nodes in a singly linked list by odd and even indices, we can use two pointers (`odd` and `even`) to build two separate lists: one for odd-indexed nodes and another for even-indexed nodes. At the end, we connect the odd-indexed list to the even-indexed list.

Here is the step-by-step solution:

---

### Approach:

1. **Edge Cases**:
   - If the list is empty or contains only one node, return the `head` as it is.

2. **Pointers Setup**:
   - Use two pointers:
     - `odd` starts at the first node.
     - `even` starts at the second node.
   - Keep track of the head of the even list (`even_head`) for later connection.

3. **Traverse and Reorder**:
   - Iterate through the list, reassigning the `next` pointers for the odd and even lists.
   - Skip alternate nodes:
     - Move `odd.next` to `odd.next.next` (next odd node).
     - Move `even.next` to `even.next.next` (next even node).
   - Update `odd` and `even` pointers accordingly.

4. **Merge Lists**:
   - After the traversal, connect the end of the odd list to the head of the even list.

5. **Return Result**:
   - Return the modified list starting from the original head.

---

### Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
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
```

---

### Example Walkthrough:

#### Example 1:
```python
Input: head = [1,2,3,4,5]
```

- **Initial Setup**:
  - `odd = 1`, `even = 2`, `even_head = 2`.

- **First Iteration**:
  - Move `odd` to 3.
  - Move `even` to 4.

- **Second Iteration**:
  - Move `odd` to 5.
  - Move `even` to `None` (end of list).

- **Final Merge**:
  - Connect 5 (end of odd list) to 2 (head of even list).

**Output**:
```python
[1,3,5,2,4]
```

#### Example 2:
```python
Input: head = [2,1,3,5,6,4,7]
```

- **Initial Setup**:
  - `odd = 2`, `even = 1`, `even_head = 1`.

- **Traversal and Reordering**:
  - Group odd: [2,3,6,7].
  - Group even: [1,5,4].

- **Final Merge**:
  - Connect 7 (end of odd list) to 1 (head of even list).

**Output**:
```python
[2,3,6,7,1,5,4]
```

---

### Complexity Analysis:

1. **Time Complexity**:
   - Each node is visited once, so the time complexity is \(O(n)\), where \(n\) is the number of nodes.

2. **Space Complexity**:
   - The solution uses only pointers and no extra data structures, so the space complexity is \(O(1)\).

This approach ensures both optimal time and space efficiency, as required.
