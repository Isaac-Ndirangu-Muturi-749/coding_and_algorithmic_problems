from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root):
    """Helper function to convert a binary tree into a list."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing 'None' values from the list to match the expected output format
    while result and result[-1] is None:
        result.pop()

    return result

def run_tests():
    solution = Solution()

    # Test case 1: Build tree from inorder and postorder
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    expected_output1 = [3, 9, 20, None, None, 15, 7]
    result1 = solution.buildTree(inorder1, postorder1)
    assert tree_to_list(result1) == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {tree_to_list(result1)}"
    print("Test case 1 passed")

    # Test case 2: Single node tree
    inorder2 = [-1]
    postorder2 = [-1]
    expected_output2 = [-1]
    result2 = solution.buildTree(inorder2, postorder2)
    assert tree_to_list(result2) == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {tree_to_list(result2)}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
