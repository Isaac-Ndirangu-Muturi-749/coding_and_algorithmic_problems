class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # Step 1: Sort the potions array
        potions.sort()
        m = len(potions)

        # Manual binary search function
        def binary_search(target):
            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Step 2: Calculate successful pairs for each spell
        result = []
        for spell in spells:
            threshold = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
            index = binary_search(threshold)
            result.append(m - index)  # Number of successful potions is the remaining ones

        return result
