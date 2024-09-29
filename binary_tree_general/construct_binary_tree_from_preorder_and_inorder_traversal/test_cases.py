from solution import Solution

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def run_tests():
    solution = Solution()

    # Test case 1
    # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]

    # Call the method and get output
    root1 = solution.buildTree(preorder1, inorder1)

    # Collect output as a list for easy comparison (level order)
    result1 = level_order_traversal(root1)
    print(f"Test case 1 output: {result1} (Expected: [3, 9, 20, None, None, 15, 7])")

    # Test case 2
    # Input: preorder = [-1], inorder = [-1]
    preorder2 = [-1]
    inorder2 = [-1]

    # Call the method and get output
    root2 = solution.buildTree(preorder2, inorder2)

    # Collect output as a list for easy comparison (level order)
    result2 = level_order_traversal(root2)
    print(f"Test case 2 output: {result2} (Expected: [-1])")

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)  # For representation of null children

    # Remove trailing Nones for clean output
    while result and result[-1] is None:
        result.pop()

    return result

if __name__ == '__main__':
    run_tests()
