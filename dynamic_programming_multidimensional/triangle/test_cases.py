from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert solution.minimumTotal(triangle1) == 11, "Test case 1 failed"

    # Test case 2
    triangle2 = [[-10]]
    assert solution.minimumTotal(triangle2) == -10, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
