Here’s an efficient stack-based solution for the problem:

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

Explanation:

Uses a stack to handle nested parentheses.

Iterates through the string while maintaining:

num: To store multi-digit numbers.

sign: Tracks the sign of the current number.

result: Stores the intermediate sum.


When encountering "(", it saves the current result and sign on the stack.

When encountering ")", it resolves the expression inside the parentheses using values from the stack.

Handles spaces by ignoring them.


This runs in O(n) time complexity, as it processes each character once.


Solution Explanation: Implementing a Basic Calculator

The problem requires evaluating a mathematical expression given as a string, following standard arithmetic rules for addition, subtraction, and parentheses. We cannot use built-in functions like eval(), so we need to manually parse and compute the expression.


---

Approach

We will use a stack to handle parentheses and signs efficiently while iterating through the string.

Key Components of the Solution:

1. Stack (stack)

Stores intermediate results and signs when encountering (.



2. Current Number (num)

Builds multi-digit numbers as we traverse the string.



3. Sign (sign)

Tracks whether the current number is positive (+1) or negative (-1).



4. Intermediate Result (result)

Keeps track of the running sum while evaluating the expression.





---

Code Walkthrough

class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to store previous results and signs
        num = 0  # Current number being formed
        sign = 1  # Current sign (1 for positive, -1 for negative)
        result = 0  # Accumulates the result

Initialize the stack, num, sign, and result.



---

Iterating Over the Characters in s

for char in s:

Loop through each character in the given string s.


1️⃣ If the character is a digit (0-9)

if char.isdigit():
                num = num * 10 + int(char)  # Build the number digit by digit

Since numbers can be multiple digits (e.g., 23 instead of 2 and 3 separately), we accumulate the number by multiplying num by 10 and adding the current digit.


2️⃣ If the character is a '+' or '-' (operator)

elif char in ["+", "-"]:
                result += sign * num  # Apply the previous number with its sign
                num = 0  # Reset num for the next number
                sign = 1 if char == "+" else -1  # Update the sign for the next number

Apply the last number by adding (+) or subtracting (-) it from result.

Reset num for the next number.

Update sign for the next number.


3️⃣ If the character is a ( (opening parenthesis)

elif char == "(":
                stack.append(result)  # Store current result before parentheses
                stack.append(sign)  # Store the current sign before parentheses
                result = 0  # Reset result inside parentheses
                sign = 1  # Reset sign inside parentheses

Store the current result and sign before entering the parentheses.

Reset result and sign to compute the expression inside the parentheses separately.


4️⃣ If the character is a ) (closing parenthesis)

elif char == ")":
                result += sign * num  # Apply the last pending number
                num = 0  # Reset num

                result *= stack.pop()  # Multiply by the sign before parentheses
                result += stack.pop()  # Add the result before parentheses

Apply the last number before closing the parentheses.

Pop and apply the sign stored before encountering (.

Pop and add the previous result stored before encountering (.



---

Final Calculation

return result + sign * num  # Apply the last pending number

After the loop, apply the last number that might still be pending.



---

Example Walkthrough

Example 1:

Input: s = "1 + 1"

Step-by-step evaluation:

1. 1 → num = 1


2. + → result = 1, reset num = 0, set sign = 1


3. 1 → num = 1


4. End of string → result = 1 + 1 = 2



✅ Output: 2


---

Example 2:

Input: s = "2-1 + 2"

Step-by-step:

1. 2 → num = 2


2. - → result = 2, reset num = 0, set sign = -1


3. 1 → num = 1


4. + → result = 2 - 1 = 1, reset num = 0, set sign = 1


5. 2 → num = 2


6. End of string → result = 1 + 2 = 3



✅ Output: 3


---

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"

Processing parentheses using stack:

1. ( → Push result = 0 and sign = 1 to stack


2. 1 → num = 1


3. + → result = 1, reset num = 0


4. ( → Push result = 1 and sign = 1 to stack


5. 4 → num = 4


6. + → result = 4, reset num = 0


7. 5 → num = 5


8. + → result = 4 + 5 = 9, reset num = 0


9. 2 → num = 2


10. ) → result = 9 + 2 = 11, multiply by stack sign, add to stack result → result = 1 + 11 = 12


11. -3 → result = 12 - 3 = 9


12. ) → Apply sign and result stored in stack → result = 9


13. + → Set sign = 1


14. ( → Push result = 9 and sign = 1 to stack


15. 6 + 8 → result = 14


16. ) → result = 9 + 14 = 23



✅ Output: 23


---

Complexity Analysis

Time Complexity: O(n)

Each character is processed at most once.


Space Complexity: O(n)

The worst case (deeply nested parentheses) requires storing intermediate results.




---

Final Thoughts

The stack efficiently handles nested parentheses and sign management.

This greedy parsing approach ensures an O(n) time complexity, making it optimal for large inputs.

Handles multi-digit numbers, spaces, and negative numbers properly.


This approach ensures correctness while being efficient and scalable.

