Here is the solution for reversing a singly linked list both iteratively and recursively in Python:

---

### **Definition for a Linked List Node**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

### **Iterative Approach**
```python
class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None  # Initialize the previous pointer as None
        current = head  # Start from the head node

        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the previous pointer to the current node
            current = next_node  # Move to the next node

        return prev  # Return the new head of the reversed list
```

---

### **Recursive Approach**
```python
class Solution:
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or contains one node
        if not head or not head.next:
            return head

        # Reverse the rest of the list
        reversed_list = self.reverseListRecursive(head.next)

        # Make the current node the tail of the reversed list
        head.next.next = head
        head.next = None  # Disconnect the current node

        return reversed_list  # Return the new head of the reversed list
```

---

### **Usage Example**
#### Example 1:
Input:
```python
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head_iterative = solution.reverseListIterative(head)
```

Output:
- The reversed list is `5 -> 4 -> 3 -> 2 -> 1`.

#### Example 2:
Input:
```python
head = ListNode(1, ListNode(2))
reversed_head_recursive = solution.reverseListRecursive(head)
```

Output:
- The reversed list is `2 -> 1`.

#### Example 3:
Input:
```python
head = None
reversed_head_iterative = solution.reverseListIterative(head)
```

Output:
- The reversed list is `None`.

---

### **Complexity Analysis**

1. **Iterative Approach**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list. Each node is visited once.
   - **Space Complexity**: \(O(1)\), as no additional memory is used aside from pointers.

2. **Recursive Approach**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list.
   - **Space Complexity**: \(O(n)\), due to the recursion stack.

Both approaches are efficient and can handle the problem's constraints.
