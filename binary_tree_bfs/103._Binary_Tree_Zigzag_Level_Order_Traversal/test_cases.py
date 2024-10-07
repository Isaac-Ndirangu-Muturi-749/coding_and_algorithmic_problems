from solution import Solution
from solution import TreeNode

def build_tree_from_list(vals):
    """Helper function to build a binary tree from a list of values using BFS"""
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()

        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1

        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1

    return root

def run_tests():
    solution = Solution()

    # Test Case 1:
    root = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]], "Test case 1 failed"

    # Test Case 2: Single node
    root = build_tree_from_list([1])
    assert solution.zigzagLevelOrder(root) == [[1]], "Test case 2 failed"

    # Test Case 3: Empty tree
    root = build_tree_from_list([])
    assert solution.zigzagLevelOrder(root) == [], "Test case 3 failed"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
