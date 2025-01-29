class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0  # Stores the current result

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build the number digit by digit
            elif char in ["+", "-"]:
                result += sign * num  # Apply the previous sign
                num = 0  # Reset the number
                sign = 1 if char == "+" else -1  # Update the sign
            elif char == "(":
                stack.append(result)  # Store current result
                stack.append(sign)  # Store current sign
                result = 0  # Reset result for new sub-expression
                sign = 1  # Reset sign
            elif char == ")":
                result += sign * num  # Apply the last pending number
                num = 0  # Reset number
                result *= stack.pop()  # Multiply with the last stored sign
                result += stack.pop()  # Add the last stored result

        return result + sign * num  # Add the last pending number
