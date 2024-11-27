class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Track the number of flowers we can plant
        length = len(flowerbed)

        for i in range(length):
            # Check if the current plot is empty and its neighbors are also empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower here
                count += 1
                if count >= n:  # Early exit if we've planted enough flowers
                    return True

        return count >= n  # Return whether we could plant at least `n` flowers
