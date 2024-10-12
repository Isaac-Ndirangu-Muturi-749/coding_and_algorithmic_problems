from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    word1_1 = "horse"
    word2_1 = "ros"
    expected_output1 = 3
    assert solution.minDistance(word1_1, word2_1) == expected_output1, f"Test case 1 failed. Expected {expected_output1}, got {solution.minDistance(word1_1, word2_1)}"

    # Test case 2
    word1_2 = "intention"
    word2_2 = "execution"
    expected_output2 = 5
    assert solution.minDistance(word1_2, word2_2) == expected_output2, f"Test case 2 failed. Expected {expected_output2}, got {solution.minDistance(word1_2, word2_2)}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
