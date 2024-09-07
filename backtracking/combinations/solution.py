class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, comb):
            # If the combination is of the right length, add it to the results
            if len(comb) == k:
                result.append(comb[:]) # or comb.copy()
                return

            # Iterate through the range and explore combinations
            for i in range(start, n + 1):
                # Add i into the combination
                comb.append(i)
                # Recurse by exploring further with i + 1
                backtrack(i + 1, comb)
                # Backtrack: remove the last added element
                comb.pop()

        result = []
        backtrack(1, [])
        return result
