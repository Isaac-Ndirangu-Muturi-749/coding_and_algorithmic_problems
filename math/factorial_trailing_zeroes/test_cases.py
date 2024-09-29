from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    n1 = 3
    output1 = solution.trailingZeroes(n1)
    expected1 = 0
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    n2 = 5
    output2 = solution.trailingZeroes(n2)
    expected2 = 1
    print(f"Test case 2: {output2} == {expected2}")

    # Test case 3
    n3 = 0
    output3 = solution.trailingZeroes(n3)
    expected3 = 0
    print(f"Test case 3: {output3} == {expected3}")

if __name__ == '__main__':
    run_tests()
