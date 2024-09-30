from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    expected_output1 = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    solution.gameOfLife(board1)
    assert board1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {board1}"
    print("Test case 1 passed")

    # Test case 2
    board2 = [[1, 1], [1, 0]]
    expected_output2 = [[1, 1], [1, 1]]
    solution.gameOfLife(board2)
    assert board2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {board2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
