from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Helper function to create a binary tree from a list (level order)
    @staticmethod
    def from_list(lst):
        if not lst:
            return None
        nodes = [None if val is None else TreeNode(val) for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

def run_tests():
    solution = Solution()

    # Test case 1
    root1 = TreeNode.from_list([1, 2, 3])
    expected_output1 = 25
    result1 = solution.sumNumbers(root1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    root2 = TreeNode.from_list([4, 9, 0, 5, 1])
    expected_output2 = 1026
    result2 = solution.sumNumbers(root2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
