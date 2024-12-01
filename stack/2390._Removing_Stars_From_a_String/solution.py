class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for char in s:
            if char == '*':
                if stack:  # Ensure the stack is not empty
                    stack.pop()  # Remove the last character
            else:
                stack.append(char)  # Add non-star character to the stack

        return ''.join(stack)  # Convert the stack to a string
