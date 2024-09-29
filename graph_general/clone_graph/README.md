To solve the problem of **deep copying a graph**, where each node contains a list of its neighbors, we can use a technique involving **DFS** (Depth-First Search) or **BFS** (Breadth-First Search). The key is to ensure that every node is copied exactly once, and all neighbor relationships are preserved.

### Approach:
1. We maintain a **hashmap (visited dictionary)** to map original nodes to their corresponding cloned nodes. This helps avoid duplicating nodes and allows reusing already cloned nodes when visiting their neighbors.
2. We can traverse the graph using either DFS or BFS, ensuring that each node and its neighbors are cloned.
3. For each node we visit, we create a new node if it hasn’t been visited, and then recursively (or iteratively) clone its neighbors.

### DFS Recursive Approach

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    visited = {}

    def dfs(node):
        # If the node is already visited, return its clone
        if node in visited:
            return visited[node]

        # Create a clone for the current node
        clone = Node(node.val)
        visited[node] = clone

        # Iterate over all the neighbors and clone them
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)
```

### Explanation:
- **Base case**: If the input node is `None`, return `None` (empty graph).
- **Visited dictionary**: It tracks nodes we've already cloned to avoid duplicating nodes during traversal.
- **DFS function**:
  - For each node, create a clone.
  - Recursively clone all of its neighbors and attach them to the cloned node’s neighbor list.
- **Return** the clone of the starting node.

### BFS Iterative Approach

An alternative method is using **BFS** to iteratively copy the graph. This approach is slightly different in that it uses a queue to traverse the graph level by level.

```python
from collections import deque

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    visited = {}

    # Start BFS from the given node
    queue = deque([node])

    # Clone the first node and add it to visited
    visited[node] = Node(node.val)

    while queue:
        current = queue.popleft()

        # Iterate over the neighbors of the node
        for neighbor in current.neighbors:
            if neighbor not in visited:
                # Clone the neighbor if it hasn't been cloned
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            # Append the cloned neighbor to the cloned current node's neighbors list
            visited[current].neighbors.append(visited[neighbor])

    # Return the cloned graph, i.e., the clone of the start node
    return visited[node]
```

### Explanation:
- **Queue**: We use a queue to traverse the graph level by level.
- For each node, we clone its neighbors if they haven’t been cloned yet and append them to the queue for further traversal.
- **Visited dictionary**: Keeps track of cloned nodes.

### Time and Space Complexity:
- **Time Complexity**: `O(V + E)` where `V` is the number of vertices (nodes) and `E` is the number of edges (neighbor relationships). This is because we visit each node once and process each edge once.
- **Space Complexity**: `O(V)` because we store each node and its clone in the visited dictionary.

### Example:

#### Example 1:

```plaintext
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

For the input graph where:
```
   1 --- 2
   |     |
   4 --- 3
```
The clone of this graph would have exactly the same structure.

#### Example 2:

```plaintext
Input: adjList = [[]]
Output: [[]]
```
The graph contains only a single node with no neighbors, and the clone will also have a single node with no neighbors.

#### Example 3:

```plaintext
Input: adjList = []
Output: []
```
The graph is empty, so the clone will also be an empty graph.

This approach ensures a deep copy of the graph while maintaining the original node structure and all neighbor relationships.
