class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, target):
            # If we have found a valid combination
            if len(path) == k and target == 0:
                result.append(path[:])
                return
            # If the combination is invalid
            if len(path) > k or target < 0:
                return

            # Explore numbers from 'start' to 9
            for i in range(start, 10):
                path.append(i)  # Choose the number
                backtrack(i + 1, path, target - i)  # Explore further
                path.pop()  # Backtrack

        backtrack(1, [], n)
        return result
