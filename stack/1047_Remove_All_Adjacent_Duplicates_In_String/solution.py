class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for char in s:
            # Remove adjacent duplicates
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        # Return the result as a string
        return ''.join(stack)
