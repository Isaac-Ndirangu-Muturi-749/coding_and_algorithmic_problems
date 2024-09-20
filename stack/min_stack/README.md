To implement a stack that supports `push`, `pop`, `top`, and retrieving the minimum element (`getMin`) in constant time, we can maintain an additional stack (`min_stack`) that keeps track of the minimum values as we perform stack operations. This way, we can ensure that both `push` and `pop` operations can be done in O(1) time while also keeping track of the minimum value at every stage.

### Approach:

- **Main Stack**: This stack will behave like a regular stack, holding all the pushed elements.
- **Min Stack**: This stack will hold the minimum element seen so far at each point in the main stack. Whenever we push a new element, we check if it’s the new minimum. If it is, we push it onto the `min_stack`. When we pop from the main stack, we also pop from the `min_stack` if the popped element is the current minimum.

### Operations:

1. **push(val)**:
   - Push `val` to the main stack.
   - Push `val` to the `min_stack` if it is smaller than or equal to the current minimum.

2. **pop()**:
   - Pop the top element from the main stack.
   - If this element is equal to the top of the `min_stack`, pop it from the `min_stack` as well.

3. **top()**:
   - Return the top element of the main stack.

4. **getMin()**:
   - Return the top element of the `min_stack` which is the current minimum.

### Code Implementation:

```python
class MinStack:

    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Min stack to keep track of the minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the value onto the min stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top element from the main stack
        if self.stack:
            popped_value = self.stack.pop()
            # If the popped value is the current minimum, pop it from the min stack
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top element of the min stack (current minimum)
        return self.min_stack[-1] if self.min_stack else None
```

### Example Walkthrough:

Given the input:

```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

1. **Initialization**:
   - Create a new MinStack: `MinStack()`
     Result: `null`

2. **Push -2**:
   - `stack = [-2]`, `min_stack = [-2]`
   - Result: `null`

3. **Push 0**:
   - `stack = [-2, 0]`, `min_stack = [-2]` (since -2 is still the minimum)
   - Result: `null`

4. **Push -3**:
   - `stack = [-2, 0, -3]`, `min_stack = [-2, -3]` (-3 is the new minimum)
   - Result: `null`

5. **getMin()**:
   - Return `-3` (current minimum from `min_stack`)
   - Result: `-3`

6. **pop()**:
   - Pop -3 from `stack` and also pop -3 from `min_stack`.
   - `stack = [-2, 0]`, `min_stack = [-2]`
   - Result: `null`

7. **top()**:
   - Return `0` (the current top of `stack`)
   - Result: `0`

8. **getMin()**:
   - Return `-2` (current minimum from `min_stack`)
   - Result: `-2`

### Time Complexity:

- **push()**: O(1)
- **pop()**: O(1)
- **top()**: O(1)
- **getMin()**: O(1)

### Space Complexity:

- O(n), where `n` is the number of elements in the stack (since both `stack` and `min_stack` store up to `n` elements).
