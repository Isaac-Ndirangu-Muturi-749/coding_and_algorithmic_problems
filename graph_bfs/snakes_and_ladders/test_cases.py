from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    board1 = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
    assert solution.snakesAndLadders(board1) == 4, "Test case 1 failed"

    # Test case 2
    board2 = [
        [-1,-1],
        [-1,3]
    ]
    assert solution.snakesAndLadders(board2) == 1, "Test case 2 failed"

    # Add more test cases if needed
    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
