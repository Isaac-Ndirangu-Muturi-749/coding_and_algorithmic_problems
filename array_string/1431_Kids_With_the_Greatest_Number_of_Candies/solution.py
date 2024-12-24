class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # Step 1: Find the maximum number of candies
        max_candies = max(candies)

        # Step 2: Calculate the result for each kid
        result = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        # Step 3: Return the result array
        return result
