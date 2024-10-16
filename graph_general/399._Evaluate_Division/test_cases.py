from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected_output1 = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    assert solution.calcEquation(equations1, values1, queries1) == expected_output1, f"Test case 1 failed"

    # Test case 2
    equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values2 = [1.5, 2.5, 5.0]
    queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected_output2 = [3.75000, 0.40000, 5.00000, 0.20000]
    assert solution.calcEquation(equations2, values2, queries2) == expected_output2, f"Test case 2 failed"

    # Test case 3
    equations3 = [["a", "b"]]
    values3 = [0.5]
    queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected_output3 = [0.50000, 2.00000, -1.00000, -1.00000]
    assert solution.calcEquation(equations3, values3, queries3) == expected_output3, f"Test case 3 failed"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
