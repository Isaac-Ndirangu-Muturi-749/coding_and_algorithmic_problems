class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)  # Increment count
                if stack[-1][1] == k:
                    stack.pop()  # Remove when count equals k
            else:
                stack.append((char, 1))  # Add new character with count 1

        # Reconstruct the string from the stack
        return ''.join(char * count for char, count in stack)
