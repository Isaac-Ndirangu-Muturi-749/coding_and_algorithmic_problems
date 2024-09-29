from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    root_data = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree(root_data)
    output = solution.levelOrder(root)
    expected = [[3], [9, 20], [15, 7]]
    print(f"Test case 1: {output} == {expected}")

    # Test case 2
    root_data = [1]
    root = create_binary_tree(root_data)
    output = solution.levelOrder(root)
    expected = [[1]]
    print(f"Test case 2: {output} == {expected}")

    # Test case 3
    root_data = []
    root = create_binary_tree(root_data)
    output = solution.levelOrder(root)
    expected = []
    print(f"Test case 3: {output} == {expected}")

if __name__ == '__main__':
    run_tests()
