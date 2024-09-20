from solution import Solution
from solution import TreeNode  # Assuming TreeNode is defined in the solution file

def list_to_tree(lst):
    """Helper function to convert a list into a binary tree."""
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

def tree_to_list(root):
    """Helper function to convert a binary tree back into a list (level order)."""
    if not root:
        return []
    result, queue = [], [root]
    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones for a cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

def run_tests():
    solution = Solution()

    # Test case 1: Invert binary tree [4,2,7,1,3,6,9]
    tree1 = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    result1 = solution.invertTree(tree1)
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(result1) == expected1, f"Test case 1 failed: Expected {expected1}, got {tree_to_list(result1)}"

    # Test case 2: Invert binary tree [2,1,3]
    tree2 = list_to_tree([2, 1, 3])
    result2 = solution.invertTree(tree2)
    expected2 = [2, 3, 1]
    assert tree_to_list(result2) == expected2, f"Test case 2 failed: Expected {expected2}, got {tree_to_list(result2)}"

    # Test case 3: Invert empty tree []
    tree3 = list_to_tree([])
    result3 = solution.invertTree(tree3)
    expected3 = []
    assert tree_to_list(result3) == expected3, f"Test case 3 failed: Expected {expected3}, got {tree_to_list(result3)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
