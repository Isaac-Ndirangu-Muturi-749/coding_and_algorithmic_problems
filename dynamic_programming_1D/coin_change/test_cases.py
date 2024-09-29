from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    output1 = solution.coinChange(coins1, amount1)
    expected1 = 3
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    coins2 = [2]
    amount2 = 3
    output2 = solution.coinChange(coins2, amount2)
    expected2 = -1
    print(f"Test case 2: {output2} == {expected2}")

    # Test case 3
    coins3 = [1]
    amount3 = 0
    output3 = solution.coinChange(coins3, amount3)
    expected3 = 0
    print(f"Test case 3: {output3} == {expected3}")

if __name__ == '__main__':
    run_tests()
