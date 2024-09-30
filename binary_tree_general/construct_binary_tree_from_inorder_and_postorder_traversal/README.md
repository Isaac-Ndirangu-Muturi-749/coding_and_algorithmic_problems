To reconstruct the binary tree from its **inorder** and **postorder** traversal arrays, we can use the following approach:

### Key Observations:
1. In **postorder traversal**, the last element is the root of the current subtree.
2. In **inorder traversal**, the elements to the left of the root are in the left subtree, and the elements to the right are in the right subtree.
3. Using the root from the postorder traversal, we can split the inorder traversal into left and right subtrees, then recursively build the tree.

### Approach:
- Start with the last element of the postorder array as the root.
- Find the position of this root in the inorder array.
- Elements to the left of this position in the inorder array form the left subtree, and elements to the right form the right subtree.
- Recursively apply the same logic to build both the left and right subtrees.
- Continue until the tree is completely reconstructed.

### Algorithm:
1. Identify the root using the last element of the postorder array.
2. Find the root's index in the inorder array.
3. Split the inorder array into left and right subtrees based on the root's index.
4. Recursively construct the left and right subtrees.
5. Return the root node.

### Code Implementation:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Dictionary to store the index of each value in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to recursively build the tree
        def build(in_left, in_right):
            # If there are no elements to construct the subtree
            if in_left > in_right:
                return None

            # Pick the last element in postorder as a root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Root splits inorder list into left and right subtrees
            index = inorder_map[root_val]

            # Build right subtree first because of postorder (L -> R -> Root)
            root.right = build(index + 1, in_right)
            # Build left subtree
            root.left = build(in_left, index - 1)

            return root

        # Start building the tree from the entire inorder range
        return build(0, len(inorder) - 1)
```

### Explanation:
1. **Inorder Map**: We create a dictionary `inorder_map` to store the index of each element in the inorder traversal for fast lookup. This allows us to quickly find the root in the inorder array.

2. **Recursion**:
   - The function `build` recursively constructs the tree using the current boundaries `in_left` and `in_right` of the inorder array.
   - The base case is when `in_left > in_right`, meaning there are no elements left to construct the subtree.
   - The root is the last element in the postorder array (we pop it from the array).
   - We find the root’s index in the inorder array to determine the boundary of the left and right subtrees.
   - We first build the right subtree, then the left subtree, as postorder traversal processes nodes in "left-right-root" order.

3. **Populating the Tree**:
   - We build the right subtree before the left because of how the postorder traversal works (the root is processed after both subtrees).
   - This ensures that we correctly reconstruct the tree as postorder pops the root after its subtrees have been processed.

### Example Walkthrough:

#### Example 1:
- **Inorder**: [9, 3, 15, 20, 7]
- **Postorder**: [9, 15, 7, 20, 3]

1. The root is `3` (last element in postorder).
2. In inorder, `3` is at index 1.
3. The elements to the left of `3` in inorder (`[9]`) form the left subtree.
4. The elements to the right of `3` in inorder (`[15, 20, 7]`) form the right subtree.
5. Recursively repeat the process for the left and right subtrees.

#### Example 2:
- **Inorder**: [-1]
- **Postorder**: [-1]
- The tree consists of a single node, so the root is `-1`.

### Time and Space Complexity:

- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. We visit each node exactly once.
- **Space Complexity**: O(n), for the recursion stack and the hash map storing the inorder indices.

This approach efficiently builds the binary tree from the given traversals.
