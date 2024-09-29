from solution import Solution, TreeNode

# Helper function to create a binary tree from a list input (level-order)
def create_binary_tree(data):
    if not data:
        return None

    nodes = [None if val is None else TreeNode(val) for val in data]

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
    root_data = [1, 2, 2, 3, 4, 4, 3]
    root = create_binary_tree(root_data)
    output = solution.isSymmetric(root)
    print(f"Test case 1: {output} == True")

    # Test case 2
    root_data = [1, 2, 2, None, 3, None, 3]
    root = create_binary_tree(root_data)
    output = solution.isSymmetric(root)
    print(f"Test case 2: {output} == False")

if __name__ == '__main__':
    run_tests()
