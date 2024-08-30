class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Dictionary to match corresponding opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Pop the topmost element if it matches the corresponding opening bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening bracket onto stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
