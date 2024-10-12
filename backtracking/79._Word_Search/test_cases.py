from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    expected_output1 = True
    assert solution.exist(board1, word1) == expected_output1, f"Test case 1 failed. Expected {expected_output1}, got {solution.exist(board1, word1)}"

    # Test case 2
    board2 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word2 = "SEE"
    expected_output2 = True
    assert solution.exist(board2, word2) == expected_output2, f"Test case 2 failed. Expected {expected_output2}, got {solution.exist(board2, word2)}"

    # Test case 3
    board3 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word3 = "ABCB"
    expected_output3 = False
    assert solution.exist(board3, word3) == expected_output3, f"Test case 3 failed. Expected {expected_output3}, got {solution.exist(board3, word3)}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
