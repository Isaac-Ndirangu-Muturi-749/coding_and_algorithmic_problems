To solve the problem of reorienting roads to ensure that all cities can travel to the capital (city 0), we can use Graph Traversal. Here's the solution approach:


---

Approach:

1. Graph Representation:

Represent the graph using adjacency lists. For each road , we store:

An edge  (representing the direction of the road).

An edge  (undirected edge to simulate traversal in both directions).




2. Traverse the Graph:

Use Breadth-First Search (BFS) or Depth-First Search (DFS) starting from city 0.

If traveling from  (opposite direction), count it as a reorientation.



3. Count the Reorientations:

During the traversal, if the direction of the edge is , it means we need to reorient the road to ensure connectivity.



4. Output:

Return the total number of reorientations.





---

Implementation (Python):

from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, True))  # True means the original road is a -> b
            graph[b].append((a, False))  # False means reverse direction
        
        # Step 2: Initialize variables
        visited = set()
        queue = deque([0])  # Start BFS from city 0
        changes = 0
        
        # Step 3: Perform BFS
        while queue:
            city = queue.popleft()
            visited.add(city)
            
            for neighbor, is_original_direction in graph[city]:
                if neighbor not in visited:
                    # Count reorientation if the direction is original (a -> b)
                    if is_original_direction:
                        changes += 1
                    queue.append(neighbor)
        
        return changes


---

Explanation of the Code:

1. Graph Construction:

Each road is stored twice:

 (as is).

 (reverse direction).




2. BFS Traversal:

Start from city 0.

For each neighbor of the current city:

If the road is in the original direction (), increment the changes counter.

Add unvisited neighbors to the queue.




3. Reorientation Counting:

A reorientation is counted only if the edge goes away from the capital in its original direction.



4. Return the Result:

Return the total number of reoriented roads.





---

Complexity Analysis:

1. Time Complexity:

: Each edge and node is processed once during the BFS traversal.



2. Space Complexity:

: For storing the graph and the BFS queue.





---

Example Walkthrough:

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3

Roads to reorient: , , .


Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2

Roads to reorient: , .


Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

No roads need to be reoriented.



---

This approach guarantees efficient and correct computation of the minimum number of edges that need reorientation.

