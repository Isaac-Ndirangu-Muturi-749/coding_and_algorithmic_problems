from collections import deque
from typing import List

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
