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
