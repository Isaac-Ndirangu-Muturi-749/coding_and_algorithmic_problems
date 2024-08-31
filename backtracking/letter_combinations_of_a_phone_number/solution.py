class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index: int, path: str):
            # If the path length equals the length of digits, add to results
            if index == len(digits):
                combinations.append(path)
                return

            # Get letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]

            # Recur for each letter in the possible letters
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        combinations = []
        backtrack(0, "")
        return combinations
