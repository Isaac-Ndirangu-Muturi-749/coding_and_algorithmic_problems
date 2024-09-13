from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    n1 = 0b00000010100101000001111010011100  # Input as binary
    assert solution.reverseBits(n1) == 964176192, "Test case 1 failed"

    # Example 2
    n2 = 0b11111111111111111111111111111101  # Input as binary
    assert solution.reverseBits(n2) == 3221225471, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
