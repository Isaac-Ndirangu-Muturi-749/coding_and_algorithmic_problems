from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert solution.canCompleteCircuit(gas, cost) == 3, "Test case 1 failed"

    # Example 2
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert solution.canCompleteCircuit(gas, cost) == -1, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
