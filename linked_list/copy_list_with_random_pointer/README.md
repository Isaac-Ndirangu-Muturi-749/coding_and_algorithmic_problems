To solve the problem of creating a deep copy of a linked list with both `next` and `random` pointers, we need to ensure that we maintain the structure and relationships between nodes in the original list while copying.

### Approach:
We can use a three-step approach to accomplish this task:

1. **Step 1: Interweaving the original and copied nodes**
   - For each node in the original list, create a new node with the same value and interweave it right after the original node. This allows us to easily assign the `random` pointers later because the copied node will be next to its original counterpart.

2. **Step 2: Assign the `random` pointers**
   - Traverse the interweaved list. For each original node, assign the `random` pointer of the copied node. If the original node's `random` pointer is not `null`, then the corresponding copied node will have a `random` pointer that points to the node right after the original's `random` node.

3. **Step 3: Restore the original list and separate the copied list**
   - Finally, restore the original list by separating the interweaved nodes. This step ensures that we get the deep copy list while maintaining the original list intact.

### Algorithm:
1. Traverse the original list and for each node, create a new node that is a copy of the original and place it right after the original node.
2. Traverse the list again to assign the `random` pointers to the new nodes.
3. Finally, restore the original list and extract the copied list.

### Code Implementation in Python:

```python
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    # Step 1: Create new nodes and interweave them with the original nodes.
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers for the new nodes.
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Restore the original list and separate the copied list.
    current = head
    copied_head = head.next
    while current:
        copied_node = current.next
        current.next = copied_node.next
        if copied_node.next:
            copied_node.next = copied_node.next.next
        current = current.next

    return copied_head
```

### Explanation:

#### Step 1: Interweaving
- We traverse the list and for each node in the original list, create a copy of that node and place it immediately after the original node. After this step, the list will look like:
    ```
    original1 -> copy1 -> original2 -> copy2 -> original3 -> copy3 -> ...
    ```

#### Step 2: Setting Random Pointers
- Now that the copied nodes are interleaved with the original nodes, we can easily set the `random` pointers. If `original.random` points to `random_original`, then `copy.random` should point to `random_original.next` (because `random_original.next` is the corresponding copy).

#### Step 3: Separate the Lists
- Once the `random` pointers are set, we need to restore the original list and extract the copied list. We accomplish this by skipping over every other node (i.e., separating the interwoven nodes back into two distinct lists: the original and the copied one).

### Time Complexity:
- **O(n)** where `n` is the number of nodes in the list. We perform three passes through the list:
  1. To create new nodes and interweave them.
  2. To set up the `random` pointers.
  3. To restore the original list and extract the copied list.

### Space Complexity:
- **O(1)** additional space (constant space), since we're only using a few pointers and no extra space proportional to the input size (the new nodes are part of the output).

### Example Walkthrough:

#### Example 1:
Input: `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`

1. **Interweaving step**:
    ```
    [7] -> [7'] -> [13] -> [13'] -> [11] -> [11'] -> [10] -> [10'] -> [1] -> [1']
    ```

2. **Setting `random` pointers**:
    ```
    [7] -> [7'] -> [13] -> [13'] -> [11] -> [11'] -> [10] -> [10'] -> [1] -> [1']
      X      X         0        0         4        4         2        2         0        0
    ```

3. **Separating lists**:
   - Original list: `[7] -> [13] -> [11] -> [10] -> [1]`
   - Copied list: `[7'] -> [13'] -> [11'] -> [10'] -> [1']`

Output:
```
[[7,null],[13,0],[11,4],[10,2],[1,0]]
```



To create a deep copy of a linked list with both `next` and `random` pointers using a **hashmap**, we can approach the problem as follows:

### Approach:
1. **Create a mapping of original nodes to their copies**:
   - Traverse the original list and create a copy of each node. Store the mapping from the original node to its copy in a hashmap. This allows us to handle `random` pointers easily since we can look up the corresponding copied node for any original node.

2. **Assign `next` and `random` pointers**:
   - Traverse the list again, and for each original node, use the hashmap to assign the `next` and `random` pointers for its corresponding copied node.

### Algorithm:
1. **First pass**: Traverse the original list and create a new node for each original node. Store the mapping from the original node to the new node in a hashmap.
2. **Second pass**: Use the hashmap to set the `next` and `random` pointers for each copied node.

### Code Implementation using Hashmap:

```python
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    # Step 1: Create a hashmap to map original nodes to their copies
    old_to_new = {}

    # First pass: Create copies of each node and map them
    current = head
    while current:
        old_to_new[current] = Node(current.val)
        current = current.next

    # Second pass: Assign next and random pointers
    current = head
    while current:
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        if current.random:
            old_to_new[current].random = old_to_new[current.random]
        current = current.next

    # Return the head of the copied linked list
    return old_to_new[head]
```

### Explanation:

1. **Creating the HashMap**:
   - We iterate through the original list and for each node, we create a new node and store the mapping of `original_node` → `new_node` in the hashmap `old_to_new`.

2. **Assigning `next` and `random` pointers**:
   - We iterate through the original list again. For each node, we set the `next` and `random` pointers of the copied node by looking up the corresponding nodes in the hashmap.

3. **Return the copied list**:
   - Once the pointers are set, we return the copied list by returning `old_to_new[head]`, which is the deep copy of the head node of the original list.

### Time Complexity:
- **O(n)**, where `n` is the number of nodes in the list. We make two passes over the list:
  1. To create a mapping of the original nodes to their corresponding copied nodes.
  2. To assign the `next` and `random` pointers using the hashmap.

### Space Complexity:
- **O(n)**, where `n` is the number of nodes in the list, since we are using a hashmap to store the mapping from original nodes to copied nodes.

### Example Walkthrough:

#### Example 1:
Input: `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`

1. **Creating the HashMap**:
   - We traverse the list and create the hashmap mapping each original node to its copy:
     ```
     {
       original_7: copy_7,
       original_13: copy_13,
       original_11: copy_11,
       original_10: copy_10,
       original_1: copy_1
     }
     ```

2. **Assigning `next` and `random` pointers**:
   - For each original node, we set the `next` and `random` pointers of the corresponding copy using the hashmap:
     - `copy_7.next = copy_13`
     - `copy_13.random = copy_7`
     - `copy_11.random = copy_1`
     - `copy_10.random = copy_11`
     - `copy_1.random = copy_7`

3. **Return the copied list**:
   - The result is the deep copied linked list:
     ```
     [[7,null],[13,0],[11,4],[10,2],[1,0]]
     ```
