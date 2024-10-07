from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    expected_output = [0, 1]
    assert solution.findOrder(numCourses, prerequisites) == expected_output, f"Test case 1 failed. Expected {expected_output}"

    # Test case 2
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected_output_1 = [0, 1, 2, 3]
    expected_output_2 = [0, 2, 1, 3]
    result = solution.findOrder(numCourses, prerequisites)
    assert result == expected_output_1 or result == expected_output_2, f"Test case 2 failed. Expected {expected_output_1} or {expected_output_2}"

    # Test case 3
    numCourses = 1
    prerequisites = []
    expected_output = [0]
    assert solution.findOrder(numCourses, prerequisites) == expected_output, f"Test case 3 failed. Expected {expected_output}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
