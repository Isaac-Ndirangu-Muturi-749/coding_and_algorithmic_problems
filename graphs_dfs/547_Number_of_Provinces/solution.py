class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                # Start a new DFS for a new province
                provinces += 1
                visited[i] = True
                dfs(i)

        return provinces
