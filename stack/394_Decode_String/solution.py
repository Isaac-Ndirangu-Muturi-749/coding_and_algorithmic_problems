class Solution:
    def decodeString(self, s: str) -> str:

        num_stack = []  # Stack to store numbers (k values)
        str_stack = []  # Stack to store strings
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # Build the current number (could be multi-digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string onto stacks
                num_stack.append(current_num)
                str_stack.append(current_string)
                # Reset current number and string
                current_num = 0
                current_string = ""
            elif char == ']':
                # Pop from stacks and construct the decoded string
                repeat_count = num_stack.pop()
                previous_string = str_stack.pop()
                current_string = previous_string + current_string * repeat_count
            else:
                # Append the current character to the current string
                current_string += char

        return current_string
