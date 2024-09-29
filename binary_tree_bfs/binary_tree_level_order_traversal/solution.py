# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize queue with root

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue node
                level.append(node.val)  # Add current node's value to the level list

                if node.left:
                    queue.append(node.left)  # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child

            result.append(level)  # Add current level's values to result

        return result
