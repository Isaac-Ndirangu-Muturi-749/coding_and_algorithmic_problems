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
