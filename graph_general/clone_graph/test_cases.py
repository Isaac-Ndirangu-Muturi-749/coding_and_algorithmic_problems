from solution import Solution

def run_tests():
    solution = Solution()
    # Add your test cases here

    # Test case 1
    adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    output1 = solution.cloneGraph(adjList1)
    expected1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    adjList2 = [[]]
    output2 = solution.cloneGraph(adjList2)
    expected2 = [[]]
    print(f"Test case 2: {output2} == {expected2}")

    # Test case 3
    adjList3 = []
    output3 = solution.cloneGraph(adjList3)
    expected3 = []
    print(f"Test case 3: {output3} == {expected3}")

if __name__ == '__main__':
    run_tests()
