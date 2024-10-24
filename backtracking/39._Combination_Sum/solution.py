class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, target, path):
            # If target becomes 0, we found a valid combination
            if target == 0:
                result.append(list(path))
                return

            # If target becomes negative, stop further exploration
            if target < 0:
                return

            # Explore all candidates starting from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                # Include the candidate and move forward
                path.append(candidates[i])
                # Continue the recursion with reduced target and same 'i' (allow repeats)
                backtrack(i, target - candidates[i], path)
                # Backtrack to explore other possibilities
                path.pop()

        candidates.sort()  # Optional, but helps with pruning
        result = []
        backtrack(0, target, [])
        return result
