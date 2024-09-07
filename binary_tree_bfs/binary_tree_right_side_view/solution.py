from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        right_view = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # If it's the last node in the current level, add it to the right view
                if i == level_size - 1:
                    right_view.append(node.val)
                # Add left and then right child to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view

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
    root = create_binary_tree([1, 2, 3, None, 5, None, 4])
    assert solution.rightSideView(root) == [1, 3, 4], "Test case 1 failed"

    # Test case 2
    root = create_binary_tree([1, None, 3])
    assert solution.rightSideView(root) == [1, 3], "Test case 2 failed"

    # Test case 3
    root = create_binary_tree([])
    assert solution.rightSideView(root) == [], "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
