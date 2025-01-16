class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Graph to store division relationships
        graph = collections.defaultdict(dict)

        # Build the graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        # Helper function to perform DFS
        def dfs(src, dst, visited):
            # If the source is not in the graph, return -1.0
            if src not in graph:
                return -1.0
            # If the destination is directly reachable, return the result
            if dst in graph[src]:
                return graph[src][dst]
            # Mark the source as visited
            visited.add(src)

            # Explore neighbors
            for neighbor in graph[src]:
                if neighbor not in visited:
                    # Perform DFS recursively
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return result * graph[src][neighbor]

            return -1.0

        # Answer the queries
        results = []
        for a, b in queries:
            if a == b:
                if a in graph:
                    results.append(1.0)  # a / a = 1.0
                else:
                    results.append(-1.0)
            else:
                results.append(dfs(a, b, set()))

        return results

