from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    expected_output1 = True
    result1 = solution.canFinish(numCourses1, prerequisites1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    expected_output2 = False
    result2 = solution.canFinish(numCourses2, prerequisites2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
