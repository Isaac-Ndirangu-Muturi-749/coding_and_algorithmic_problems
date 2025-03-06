class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
        # Perform depth-first search to find the lowest common ancestor.
        def dfs(current_node):
            # Base case: If current node is None or in target nodes set, return it.
            if current_node is None or current_node in target_nodes_set:
                return current_node

            # Recursively search the left and right subtrees.
            left_ancestor = dfs(current_node.left)
            right_ancestor = dfs(current_node.right)

            # If both left and right are not None, current node is the lowest common ancestor.
            if left_ancestor and right_ancestor:
                return current_node

            # Otherwise, return the non-None value or None.
            return left_ancestor or right_ancestor

        # Convert the list of nodes to a set for faster lookup.
        # Note that the original code used node.val, assuming unique values for simplicity.
        # Here we use the nodes themselves for the matching, which is more general.
        target_nodes_set = set(nodes)

        # Start the depth-first search from the root.
        return dfs(root)
