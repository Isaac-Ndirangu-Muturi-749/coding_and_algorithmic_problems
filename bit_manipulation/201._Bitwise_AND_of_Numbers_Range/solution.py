class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        shift = 0
        # Find the common prefix by shifting right until left equals right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Shift left to restore the common prefix to its original magnitude
        return left << shift
