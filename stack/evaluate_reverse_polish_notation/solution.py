class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token in "+-*/":
                # Pop two numbers from the stack
                b = stack.pop()
                a = stack.pop()

                # Perform the operation
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    # Perform integer division with truncation toward zero
                    result = int(a / b)

                # Push the result back onto the stack
                stack.append(result)
            else:
                # If it's a number, convert it to an integer and push it to the stack
                stack.append(int(token))

        # The final result will be the only item left in the stack
        return stack[0]
