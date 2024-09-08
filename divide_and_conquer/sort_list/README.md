To sort a linked list in ascending order, you can implement merge sort, which is a stable sorting algorithm commonly used for linked lists because of its O(n log n) time complexity and O(1) space complexity (since linked lists are naturally easy to split and merge without extra space).

Here’s a Python implementation to sort a linked list:

### Solution:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node, return the head
        if not head or not head.next:
            return head

        # Split the list into two halves using the slow and fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the list into two parts
        mid = slow.next
        slow.next = None

        # Sort each half recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to act as a starting point for the merged list
        dummy = ListNode()
        current = dummy

        # Merge two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach the remaining elements from either list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        # Return the sorted list, starting from dummy's next node
        return dummy.next
```

### Explanation:

1. **Base Case**: If the list is empty or has only one node, it’s already sorted, so return it directly.
2. **Splitting the List**: We use the slow and fast pointer technique to find the middle of the list. Slow pointer moves one step at a time, and the fast pointer moves two steps at a time. When the fast pointer reaches the end, the slow pointer will be at the middle of the list.
3. **Sorting Each Half**: Recursively call `sortList` on the left and right halves.
4. **Merging**: The `merge` function merges two sorted linked lists into one sorted list.

### Test Cases:

You can test the solution with the following helper functions and test cases:

```python
# Helper function to create a linked list from a list.
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list.
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def run_tests():
    solution = Solution()

    # Test case 1
    head = create_linked_list([4, 2, 1, 3])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: [1, 2, 3, 4]

    # Test case 2
    head = create_linked_list([-1, 5, 3, 4, 0])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: [-1, 0, 3, 4, 5]

    # Test case 3
    head = create_linked_list([])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: []

if __name__ == '__main__':
    run_tests()
```

### Example Output:
```python
[1, 2, 3, 4]
[-1, 0, 3, 4, 5]
[]
```

### Complexity:
- **Time Complexity**: O(n log n), where `n` is the number of nodes in the linked list. This is due to the divide-and-conquer approach used in merge sort.
- **Space Complexity**: O(log n) due to the recursion stack in the merge sort algorithm.



To sort a linked list in \(O(n \log n)\) time and \(O(1)\) space, we can use **merge sort** with a bottom-up approach instead of the recursive top-down approach. The recursive approach uses \(O(\log n)\) space for the recursion stack, but the iterative, bottom-up approach avoids recursion, thus achieving \(O(1)\) additional space.

### Key Idea:
- **Bottom-Up Merge Sort**: Instead of recursively dividing the list, we iteratively merge sublists of increasing sizes (1, 2, 4, 8, etc.) until the entire list is sorted.
- We can achieve constant space by working directly on the original list, rearranging the nodes in place, and using only a few pointers to track the sublists as we merge.

### Plan:
1. **Iterate through increasing sublist sizes**: First, merge sublists of size 1, then size 2, then size 4, and so on, doubling the size of sublists each time.
2. **Merge adjacent sublists**: In each iteration, we go through the entire list and merge adjacent sublists of the current size.
3. **Use helper functions**: We’ll need functions to split the list into two halves of a given size and to merge two sorted sublists.

### Implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Get the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # Dummy node to serve as the starting point of the sorted list
        dummy = ListNode(0)
        dummy.next = head

        # Iteratively merge sublists of size 1, 2, 4, 8, ...
        size = 1
        while size < length:
            tail = dummy
            current = dummy.next

            while current:
                left = current
                right = self.split(left, size)
                current = self.split(right, size)
                merged = self.merge(left, right)
                tail.next = merged
                while tail.next:
                    tail = tail.next

            size *= 2

        return dummy.next

    def split(self, head: ListNode, size: int) -> ListNode:
        """Split the list after 'size' nodes and return the start of the next sublist."""
        current = head
        for i in range(size - 1):
            if current and current.next:
                current = current.next
            else:
                break

        if not current:
            return None

        next_sublist = current.next
        current.next = None
        return next_sublist

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists and return the head."""
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next
```

### Explanation:

1. **Get the length of the linked list**: We first iterate through the list to calculate its length. This allows us to know how many times we need to double the sublist size during sorting.

2. **Iteratively sort the list**:
   - We start with sublists of size 1, then double the size in each iteration (1, 2, 4, 8, ...).
   - In each iteration, we split the list into multiple pairs of sublists of the current size, and we merge them using the `merge` function.

3. **Split function**: This function splits a linked list into two parts. The first part is of the given size, and it returns the start of the second part.

4. **Merge function**: This function merges two sorted linked lists and returns the sorted result.

5. **Dummy node**: We use a dummy node to make it easier to handle the start of the merged lists without special cases.

### Time Complexity:
- **O(n \log n)**: Each iteration merges sublists, and the size of the sublists doubles after each iteration. Since each merge operation takes \(O(n)\) time and there are \(O(\log n)\) iterations, the total time complexity is \(O(n \log n)\).

### Space Complexity:
- **O(1)** additional space: We use constant space aside from the input list itself (no recursion, just a few pointers).

### Example Usage:

```python
# Helper function to create a linked list from a list.
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list.
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def run_tests():
    solution = Solution()

    # Test case 1
    head = create_linked_list([4, 2, 1, 3])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: [1, 2, 3, 4]

    # Test case 2
    head = create_linked_list([-1, 5, 3, 4, 0])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: [-1, 0, 3, 4, 5]

    # Test case 3
    head = create_linked_list([])
    result = solution.sortList(head)
    print(linked_list_to_list(result))  # Output: []

if __name__ == '__main__':
    run_tests()
```

### Example Output:
```python
[1, 2, 3, 4]
[-1, 0, 3, 4, 5]
[]
```


Let’s break down the `merge` function, which merges two sorted linked lists (`l1` and `l2`) into one sorted list.

### Goal:
- Merge two sorted linked lists into a single sorted linked list.

### Step-by-step Explanation:

1. **Create a Dummy Node**:
   ```python
   dummy = ListNode()
   current = dummy
   ```
   - **Purpose**: The `dummy` node is a placeholder to make it easier to return the head of the merged list later. The merged list will start at `dummy.next`.
   - `current` is a pointer that will traverse the new merged list as we build it.

2. **Iterate and Compare Nodes**:
   ```python
   while l1 and l2:
       if l1.val < l2.val:
           current.next = l1
           l1 = l1.next
       else:
           current.next = l2
           l2 = l2.next
       current = current.next
   ```
   - **Loop condition**: The loop runs as long as both `l1` and `l2` are non-empty (i.e., not `None`).
   - **Comparison**: For each iteration:
     - Compare the current node values of `l1` and `l2`.
     - Whichever node has the smaller value gets linked to the `current` pointer of the merged list.
     - After linking, move the pointer (`l1` or `l2`) to the next node.
   - **Move the merged list forward**: After assigning the next node, update `current` to point to this new node.

3. **Attach Remaining Nodes**:
   ```python
   if l1:
       current.next = l1
   elif l2:
       current.next = l2
   ```
   - After the while loop exits, one of the lists (`l1` or `l2`) might still have remaining nodes. Since the lists are sorted, these remaining nodes are already in order.
   - Attach the remaining portion of the non-empty list (`l1` or `l2`) directly to the `current.next` pointer.

4. **Return the Merged List**:
   ```python
   return dummy.next
   ```
   - The merged list starts from `dummy.next`, since `dummy` is just a placeholder.
   - Return `dummy.next`, which points to the head of the merged list.

### Example Walkthrough:

Let’s merge the two lists:
- `l1 = [1 -> 3 -> 5]`
- `l2 = [2 -> 4 -> 6]`

1. **First iteration**:
   - Compare `1` and `2`:
     - `1 < 2`, so add `1` from `l1` to the merged list.
     - Move `l1` to `3`.

2. **Second iteration**:
   - Compare `3` and `2`:
     - `2 < 3`, so add `2` from `l2` to the merged list.
     - Move `l2` to `4`.

3. **Third iteration**:
   - Compare `3` and `4`:
     - `3 < 4`, so add `3` from `l1` to the merged list.
     - Move `l1` to `5`.

4. **Fourth iteration**:
   - Compare `5` and `4`:
     - `4 < 5`, so add `4` from `l2` to the merged list.
     - Move `l2` to `6`.

5. **Fifth iteration**:
   - Compare `5` and `6`:
     - `5 < 6`, so add `5` from `l1` to the merged list.
     - Move `l1` to `None`.

6. **Attach remaining**:
   - `l1` is empty, but `l2` still has `6`. Attach `6` to the merged list.

7. **Return the merged list**:
   - The merged list is `[1 -> 2 -> 3 -> 4 -> 5 -> 6]`.

### Time and Space Complexity:

- **Time Complexity**: O(m + n), where `m` is the length of `l1` and `n` is the length of `l2`. We traverse both lists exactly once.
- **Space Complexity**: O(1), as we only use constant extra space for the dummy node and pointers (excluding the input space).



Let's break down the `sortList` function, which sorts a linked list using the **merge sort** algorithm. Here's a step-by-step explanation:

### 1. **Base Case**:
```python
if not head or not head.next:
    return head
```
- If the list is empty (`head == None`) or it has only one node (`head.next == None`), then the list is already sorted, so just return the `head`.

### 2. **Split the List**:
```python
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
- To split the linked list into two halves, the **slow and fast pointer** technique is used:
  - **Slow pointer** moves one step at a time.
  - **Fast pointer** moves two steps at a time.
- By the time the fast pointer reaches the end of the list, the slow pointer will be at the midpoint. This ensures that the list is split in half.

### 3. **Divide the List**:
```python
mid = slow.next
slow.next = None
```
- After finding the midpoint using the slow pointer, we store the start of the second half in `mid` and break the list into two halves by setting `slow.next = None`.

### 4. **Recursive Sort**:
```python
left = self.sortList(head)
right = self.sortList(mid)
```
- The function is called recursively on both halves (`left` and `right`), which continue to split the list until the base case (single node or empty) is reached.

### 5. **Merge the Sorted Halves**:
```python
return self.merge(left, right)
```
- Once the two halves (`left` and `right`) are sorted, they are merged together using the `merge` function (assuming it's implemented similarly to the function you've shared previously).

This merge step combines the two sorted lists into one sorted linked list.

### Full Example Walkthrough:

Let’s consider a linked list:
```
4 -> 2 -> 1 -> 3
```

1. **First Call to `sortList(4 -> 2 -> 1 -> 3)`**:
   - The list is split into two halves: `4 -> 2` and `1 -> 3`.
   - `left = sortList(4 -> 2)` and `right = sortList(1 -> 3)`.

2. **Sorting the Left Half `sortList(4 -> 2)`**:
   - This list is split into `4` and `2`.
   - `left = sortList(4)` and `right = sortList(2)` (both single-node lists, so base case).
   - Merge `4` and `2`, resulting in `2 -> 4`.

3. **Sorting the Right Half `sortList(1 -> 3)`**:
   - This list is split into `1` and `3`.
   - `left = sortList(1)` and `right = sortList(3)` (both single-node lists, so base case).
   - Merge `1` and `3`, resulting in `1 -> 3`.

4. **Final Merge**:
   - Merge the two halves `2 -> 4` and `1 -> 3`:
     - Compare `2` and `1`: Add `1` to the merged list.
     - Compare `2` and `3`: Add `2` to the merged list.
     - Compare `4` and `3`: Add `3` to the merged list.
     - Add `4` to the merged list as it's the only remaining node.
   - Final sorted list: `1 -> 2 -> 3 -> 4`.

### Time and Space Complexity:

- **Time Complexity**: O(n log n), where `n` is the number of nodes in the linked list.
  - The list is split into halves recursively, which takes O(log n), and merging two halves takes O(n).

- **Space Complexity**: O(log n), due to the recursive call stack. The space complexity could be reduced to O(1) in an iterative solution.



It seems like you're working on testing the `Solution` class with the `sortList` method for sorting a linked list. Here’s a slightly modified version of your test script that includes the necessary `assert` statements to validate the expected outputs for each test case.

```python
from solution import Solution, ListNode

# Helper function to create a linked list from a list.
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list.
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def run_tests():
    solution = Solution()

    # Test case 1
    head = create_linked_list([4, 2, 1, 3])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [1, 2, 3, 4], f"Test case 1 failed: {linked_list_to_list(result)}"

    # Test case 2
    head = create_linked_list([-1, 5, 3, 4, 0])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [-1, 0, 3, 4, 5], f"Test case 2 failed: {linked_list_to_list(result)}"

    # Test case 3
    head = create_linked_list([])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [], f"Test case 3 failed: {linked_list_to_list(result)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
```

### What was changed:
- Added `assert` statements to automatically check if the output of the `sortList` method matches the expected result. If the result is not as expected, it will raise an `AssertionError` and indicate which test case failed.

### How it works:
1. **`create_linked_list`**: Converts a list of values into a linked list.
2. **`linked_list_to_list`**: Converts a linked list back into a Python list to easily compare the results.
3. **`run_tests`**: Tests the `sortList` function for several cases. Each test uses `assert` to check if the output matches the expected result.
4. **`assert`**: If the output is not as expected, it raises an error and specifies which test failed.

### Example Usage:
When you run this, it will print `"All test cases passed!"` if everything works as expected. Otherwise, it will show an error for the test case that failed.
