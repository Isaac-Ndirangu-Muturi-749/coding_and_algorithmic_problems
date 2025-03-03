class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        sqrt_n = int(n ** 0.5)

        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i

        for i in range(sqrt_n, 0, -1):
            if n % i == 0 and i != n // i:
                count += 1
                if count == k:
                    return n // i

        return -1
