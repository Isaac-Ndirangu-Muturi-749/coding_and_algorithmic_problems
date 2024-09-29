from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    points = [[10,16], [2,8], [1,6], [7,12]]
    output = solution.findMinArrowShots(points)
    print(f"Test case 1: {output} == 2")

    # Test case 2
    points = [[1,2], [3,4], [5,6], [7,8]]
    output = solution.findMinArrowShots(points)
    print(f"Test case 2: {output} == 4")

    # Test case 3
    points = [[1,2], [2,3], [3,4], [4,5]]
    output = solution.findMinArrowShots(points)
    print(f"Test case 3: {output} == 2")

if __name__ == '__main__':
    run_tests()
