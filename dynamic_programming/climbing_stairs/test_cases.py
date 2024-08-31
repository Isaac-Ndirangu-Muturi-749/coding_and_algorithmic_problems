from solution import Solution

def run_tests():
    solution = Solution()

    test_cases = [
        (1, 1),  # n = 1, expected = 1
        (2, 2),  # n = 2, expected = 2
        (3, 3),  # n = 3, expected = 3
        (5, 8),  # n = 5, expected = 8
        (10, 89),  # n = 10, expected = 89
        (20, 10946),  # n = 20, expected = 10946
        (30, 1346269),  # n = 30, expected = 1346269
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = solution.climbStairs(n)
        assert result == expected, f"Test case {i + 1} failed: for n = {n}, expected {expected} but got {result}"
        print(f"Test case {i + 1} passed.")

if __name__ == "__main__":
    run_tests()
