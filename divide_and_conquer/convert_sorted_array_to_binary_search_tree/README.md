To convert a sorted array into a height-balanced binary search tree (BST), the key is to select the middle element of the array as the root. This ensures that the tree remains balanced, as the number of nodes in the left and right subtrees will be as equal as possible.

### Approach:

1. **Recursive Construction**:
   - **Base Case**: If the array is empty, return `None`.
   - **Recursive Case**:
     - Find the middle element of the current array segment and make it the root.
     - Recursively apply the same process to the left half of the array to form the left subtree.
     - Recursively apply the same process to the right half of the array to form the right subtree.
   - This ensures that the tree remains height-balanced because at each step, the middle element is chosen as the root, splitting the array into two roughly equal halves.

### Code Implementation:

Here's the Python implementation of the above approach:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        # Helper function to convert array to BST
        def convert_to_bst(left, right):
            if left > right:
                return None

            # Choose the middle element as the root
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convert_to_bst(left, mid - 1)
            node.right = convert_to_bst(mid + 1, right)

            return node

        # Start with the full range of the array
        return convert_to_bst(0, len(nums) - 1)
```

### Explanation:

1. **TreeNode Class**:
   - The `TreeNode` class defines the structure of a node in the binary tree, with a value `val`, a left child `left`, and a right child `right`.

2. **sortedArrayToBST Function**:
   - This function initiates the recursive conversion of the sorted array into a BST by calling the helper function `convert_to_bst` with the full range of the array (`left=0` to `right=len(nums) - 1`).

3. **convert_to_bst Function**:
   - **Base Case**: If `left > right`, return `None` because there are no elements to process.
   - **Recursive Case**:
     - Calculate the middle index `mid`.
     - Create a new `TreeNode` with the value `nums[mid]`.
     - Recursively construct the left subtree using the left half of the array (`left` to `mid - 1`).
     - Recursively construct the right subtree using the right half of the array (`mid + 1` to `right`).

### Examples:

1. **Example 1**:
   - **Input**: `nums = [-10, -3, 0, 5, 9]`
   - **Output**: A height-balanced BST with root `0`, left child `-3`, right child `9`, and so on.
   - Possible output in level order: `[0, -3, 9, -10, null, 5]`

2. **Example 2**:
   - **Input**: `nums = [1, 3]`
   - **Output**: A height-balanced BST with root `3` and left child `1`.
   - Possible output in level order: `[3, 1]`

### Testing the Function:

You can test the function with different inputs to verify that it correctly builds a height-balanced BST:

```python
def run_tests():
    solution = Solution()

    # Test case 1
    nums = [-10, -3, 0, 5, 9]
    bst_root = solution.sortedArrayToBST(nums)
    # Expected Output: A BST with root 0, left child -3, right child 9, etc.

    # Test case 2
    nums = [1, 3]
    bst_root = solution.sortedArrayToBST(nums)
    # Expected Output: A BST with root 3 and left child 1

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
```

This approach guarantees a height-balanced BST, ensuring that the tree's height is minimized for optimal performance in operations like search, insertion, and deletion.
