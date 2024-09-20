from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: A 4x4 board with some surrounded 'O' regions
    board1 = [["X","X","X","X"],
              ["X","O","O","X"],
              ["X","X","O","X"],
              ["X","O","X","X"]]

    solution.solve(board1)

    expected1 = [["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","O","X","X"]]

    assert board1 == expected1, f"Test case 1 failed: Expected {expected1}, got {board1}"

    # Test case 2: A 1x1 board with no surrounded regions
    board2 = [["X"]]

    solution.solve(board2)

    expected2 = [["X"]]

    assert board2 == expected2, f"Test case 2 failed: Expected {expected2}, got {board2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
