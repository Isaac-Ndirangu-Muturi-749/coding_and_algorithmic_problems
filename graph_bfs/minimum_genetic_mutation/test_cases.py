from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Simple mutation sequence with 1 step
    startGene1 = "AACCGGTT"
    endGene1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    result1 = solution.minMutation(startGene1, endGene1, bank1)
    expected1 = 1
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Mutation sequence with 2 steps
    startGene2 = "AACCGGTT"
    endGene2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    result2 = solution.minMutation(startGene2, endGene2, bank2)
    expected2 = 2
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    # You can add more test cases here

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
