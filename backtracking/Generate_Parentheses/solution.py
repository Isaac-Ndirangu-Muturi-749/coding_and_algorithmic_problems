class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # Helper function for backtracking
        def backtrack(current_string, open_count, close_count):
            # If the current string has reached the maximum length, add it to the result
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            # Add '(' if we still have available '(' to add
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)

            # Add ')' if there are more '(' used than ')' (to maintain valid parentheses)
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)

        # Start the backtracking process with an empty string and 0 open/close counts
        backtrack('', 0, 0)
        return result
