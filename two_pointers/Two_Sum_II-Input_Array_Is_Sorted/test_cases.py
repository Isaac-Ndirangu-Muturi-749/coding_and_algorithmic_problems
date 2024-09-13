from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(numbers1, target1)
    assert result1 == [1, 2], f"Test case 1 failed: Expected [1, 2], got {result1}"

    # Test case 2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = solution.twoSum(numbers2, target2)
    assert result2 == [1, 3], f"Test case 2 failed: Expected [1, 3], got {result2}"

    # Test case 3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = solution.twoSum(numbers3, target3)
    assert result3 == [1, 2], f"Test case 3 failed: Expected [1, 2], got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
