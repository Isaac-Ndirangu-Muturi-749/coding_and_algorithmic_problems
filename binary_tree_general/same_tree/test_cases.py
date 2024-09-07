from solution import Solution, TreeNode


# Helper function to create a binary tree from a list.
def create_binary_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root

def run_tests():
    solution = Solution()

    # Test case 1
    p = create_binary_tree([1, 2, 3])
    q = create_binary_tree([1, 2, 3])
    assert solution.isSameTree(p, q) == True, "Test case 1 failed"

    # Test case 2
    p = create_binary_tree([1, 2])
    q = create_binary_tree([1, None, 2])
    assert solution.isSameTree(p, q) == False, "Test case 2 failed"

    # Test case 3
    p = create_binary_tree([1, 2, 1])
    q = create_binary_tree([1, 1, 2])
    assert solution.isSameTree(p, q) == False, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
