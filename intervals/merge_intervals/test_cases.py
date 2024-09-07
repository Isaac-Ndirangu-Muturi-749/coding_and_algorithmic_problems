from solution import Solution

def run_tests():
    solution = Solution()

    # Define test cases and expected results
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]])
    ]

    # Iterate through test cases
    for i, (intervals, expected) in enumerate(test_cases):
        result = solution.merge(intervals)
        print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Input: {intervals}")
        print(f"Expected Output: {expected}")
        print(f"Your Output: {result}")
        print()  # Blank line for readability

if __name__ == '__main__':
    run_tests()
